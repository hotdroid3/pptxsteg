from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes

class Encryptor():
	"""Wrapper class for AES encryption methods."""
	def __init__(self):
		super().__init__()
		self._key = get_random_bytes(32)
		self._mode = AES.MODE_EAX
		self._nonce = get_random_bytes(16)
		self._mac_len = 16
		self._cipher = AES.new(self.key, self.mode, nonce=self.nonce, mac_len=self.mac_len)
	
	@property
	def key(self):
		return self._key

	@property
	def mode(self):
		return self._mode
	
	@property
	def nonce(self):
		return self._nonce

	@property
	def mac_len(self):
		return self._mac_len
	
	@property
	def cipher(self):
		return self._cipher

	def encrypt_and_sign(self, data):
		"""Wrapper method to encrypt and digest data passed in.
		Returns ciphertext and a tag.
		"""
		return self.cipher.encrypt_and_digest(data)
	

class Decryptor():
	"""Wrapper class for AES decryption methods."""
	def __init__(self, key, nonce):
		super().__init__()
		self._mode = AES.MODE_EAX
		self._mac_len = 16
		self._cipher = AES.new(key, self.mode, nonce=nonce, mac_len=self.mac_len)

	@property
	def mode(self):
		return self._mode
	
	@property
	def mac_len(self):
		return self._mac_len

	@property
	def cipher(self):
		return self._cipher

	def decrypt_and_verify(self, ciphertext, tag):
		"""Wrapper method to decrypt and verify authenticity of ciphertext.
		Raises ValueError if ciphertext is not authentic.
		"""
		data = self.cipher.decrypt_and_verify(ciphertext, tag)
		return data

	
		