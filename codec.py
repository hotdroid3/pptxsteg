from comdecom import CompressorDecompressor as comdecom
from comdecom import CompressionError
from encdec import Encryptor, Decryptor
import lzma
import os

class EncoderDecoder():
	"""Contains static methods for encoding and decoding"""
	def __init__(self):
		super().__init__()

	@staticmethod
	def encode_from_file(file_name, encryption = False):
		"""Receives the name of a file containing steganograms
		and encodes the file into a format to be embedded into the PowerPoint file,
		returning the encoded file object.
		"""
		secret_file_bytes = b''
		hex_strings = []

		if len(file_name) > 256:
			raise FileNameTooLongError(len(file_name))
		else:
			file_name_bytes = [char.encode() for char in os.path.basename(file_name)]
			file_name_bytes = b''.join(file_name_bytes)
			file_name_length = len(os.path.basename(file_name)) - 1
			file_name_length = bytes([file_name_length])

		try:
			with open(file_name, 'rb') as secret_file:
				secret_file_bytes = secret_file.read()
		except FileNotFoundError:
			print("FileNotFoundError: Please enter a proper file name!")
			raise FileNotFoundError

		secret_file_bytes = b''.join([secret_file_bytes, file_name_bytes, file_name_length])

		if encryption:
			encryptor = Encryptor()
			secret_file_bytes, tag = encryptor.encrypt_and_sign(secret_file_bytes)
			secret_file_bytes = b''.join([secret_file_bytes, tag, encryptor.nonce])

		try:
			secret_file_bytes_compressed = comdecom.compress(secret_file_bytes)
		except lzma.LZMAError as err:
			print(err)
			secret_file_bytes = b''.join([secret_file_bytes, b'n'])
		except CompressionError as err:
			print(err)
			secret_file_bytes = b''.join([secret_file_bytes, b'n'])
		else:
			secret_file_bytes = b''.join([secret_file_bytes_compressed, b'c'])

		hex_strings = [secret_file_bytes[i:i+1].hex() for i in range(0, len(secret_file_bytes))]
		
		if encryption:
			return (hex_strings, encryptor.key)
		else:
			return hex_strings

	@staticmethod
	def decode_to_file(hex_strings, decryption=False, key=None):
		"""Receives a list of hex strings; each hex string in the list is converted into a byte,
		the list of bytes are then concatenated into a single bytes object;
		checks if the bytes were compressed; if compressed, bytes are decompressed, if not,
		the bytes are not decompressed; 
		if the bytes were encrypted, bytes are decrypted,
		the bytes object is then written to file_name.
		"""
		compressed = False
		if hex_strings[-1] == '63':
			del hex_strings[-1]
			compressed = True
		elif hex_strings[-1] == '6e':
			del hex_strings[-1]
			compressed = False

		secret_file_bytes = [bytes.fromhex(hex_str) for hex_str in hex_strings]
		secret_file_bytes = b''.join(secret_file_bytes)

		if compressed:
			secret_file_bytes = comdecom.decompress(secret_file_bytes)

		if decryption:
			if key is None:
				raise ValueError('ValueError: key is not provided!')
			else:
				nonce = secret_file_bytes[-16:]
				tag = secret_file_bytes[-32:-16]
				secret_file_bytes = secret_file_bytes[0:-32]
				decryptor = Decryptor(key,nonce)
				secret_file_bytes = decryptor.decrypt_and_verify(secret_file_bytes, tag)

		file_name_length = int.from_bytes(secret_file_bytes[-1:], byteorder = 'big')
		file_name_length += 1

		file_name_partition = (len(secret_file_bytes) - 1 - file_name_length), -1
		file_name = secret_file_bytes[file_name_partition[0]:file_name_partition[1]]
		file_name = file_name.decode()

		secret_file_bytes = secret_file_bytes[0: file_name_partition[0]]

		output_file_name = 'output\\' + os.path.basename(file_name) 
		with open(output_file_name, 'wb') as secret_file:
			secret_file.write(secret_file_bytes)

	@staticmethod
	def encode_from_string(secret_string):
		"""Receives secret_string and returns a list of hex strings,
		with each hex string representing and character in the original secret_string.
		"""
		hex_strings = [char.encode().hex() for char in secret_string]
		return hex_strings

	@staticmethod
	def decode_to_string(hex_strings):
		"""Receives a list of hex strings, converts each hex string into the character that it represents,
		concatenates all the characters together to form the steganographic string.
		"""
		secret_string = [(bytes.fromhex(hex_str)).decode() for hex_str in hex_strings]
		secret_string = ''.join(secret_string)
		return secret_string

class Error(Exception):
	"""Base class for exceptions in this module."""
	pass

class FileNameTooLongError(Error):
	"""Exception raised when the file name provided is too long."""
	def __init__(self, file_name_length):
		super().__init__()
		self.file_name_length = file_name_length

	def __str__(self):
		error_message = 'FileNameTooLongError: length of file name is too long!\n'
		return error_message + 'File Name Length: {} characters'.format(self.file_name_length)