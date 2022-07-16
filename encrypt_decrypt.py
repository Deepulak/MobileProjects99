from cryptography.fernet import Fernet

# Generate key
def generate_key():
	key = Fernet.generate_key()
	with open('mykey.key', 'wb') as mykey:
		mykey.write(key)

# load key
def load_key():
	with open('mykey.key', 'rb') as mykey:
		key = mykey.read()
		return key


# Encrypt file 
def encrypt_file(filename):
	# First load the key
	key = load_key()

	f = Fernet(key)
	# open original file
	with opne(filename, 'rb') as original_file:
		original = original_file.read()
	enc_file = "enc"+str(filename)
	# encrypt and save the new file
	encrypted = f.encrypt(original)
	with open(enc_file, 'wb') as encrypted_file:
		encrypted_file.write(encrypted)

	print("file is encrypted and save as "+enc_file)

# decrypt file
def decrypt_file(filename):
	# First load the key
	key = load_key()

	f = Fernet(key)
	# open / read encrypt file
	with oprn(filename, 'rb') as encrypted_file:
		encrypted = encrypted_file.read()

	dec_file = "dec"+str(filename)
	# decrypt file and save it
	decrypted = f.decrypt(encrypted)
	with open(dec_file, 'wb') as decrypted_file:
		decrypted_file.write(decrypted)
	print("file is decrypted and save as "+dec_file)