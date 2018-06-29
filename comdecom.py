import lzma

class CompressorDecompressor():
	"""Wrapper class for LZMA compression and decompression methods"""
	
	def __init__(self):
		super().__init__()

	@staticmethod
	def compress(byte_object):
		result = lzma.compress(byte_object, preset = 9)
		if len(result) > len(byte_object):
			raise CompressionError(len(result), len(byte_object))
		else:
			# print(len(result))
			# print(len(byte_object))
			return result

	@staticmethod
	def decompress(byte_object):
		return lzma.decompress(byte_object)

class Error(Exception):
	"""Base class for exceptions in this module."""
	pass

class CompressionError(Error):
	"""Exception raised when the compressed bytes object is larger than the original bytes object"""
	def __init__(self, compressed_bytes_length, uncompressed_bytes_length):
		super().__init__()
		self.compressed_bytes_length = compressed_bytes_length
		self.uncompressed_bytes_length = uncompressed_bytes_length

	def __str__(self):
		error_message = 'CompressionError: compressed object larger than original object, using original object instead!\n'
		uncompressed_bytes_length = 'Uncompressed Bytes Length: {} bytes\n'.format(self.uncompressed_bytes_length)
		compressed_bytes_length = 'Compressed Bytes Length: {} bytes'.format(self.compressed_bytes_length)	
		return error_message + uncompressed_bytes_length + compressed_bytes_length
