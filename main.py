from simplersa import KeyPair

bit_length = input("# of bits for your prime number choices: ")

my_super_secure_keypair = KeyPair(int(bit_length))

publickey = my_super_secure_keypair.publickey
privatekey = my_super_secure_keypair.privatekey

print("Public Key (N): {} [RSA {}-bit]".format(publickey.n, privatekey.d.bit_length()))
print("Private Key (D): {}".format(privatekey.d))

sample_message = "RSA is easy!"
print("Plain Text Message: {}".format(sample_message))

encrypted = publickey.encrypt(sample_message)
print("Cipher Text: {}".format(str(encrypted)))

print("Decrypted Message: {}".format(privatekey.decrypt(encrypted.ciphertext)))


print("\nNow, let's crack this message using classical computing")

# Brute Force Attack - Classical

import math
import gmpy
import numpy as np
import time

def custom_decrypt(n, d, ciphertext):
	plain = [chr(pow(char, d, n)) for char in ciphertext]
	return ''.join(plain)

def find_p_candidate(c):
	for i in range(c, 2, -1):
		if(i % 2 == 0):
			pass
		else:
			if(n % i == 0):
				print("(P) Found!: {}".format(i))
				return i
			else:
				pass
	return None

def calculate_private_key(n, p):
	q = n // p
	phin = gmpy.mpz((p-1) * (q-1))
	d = gmpy.invert(gmpy.mpz(e), phin)
	return d

time1 = time.time()
c = math.floor(math.sqrt(publickey.n))
n = publickey.n
e = publickey.e

p = find_p_candidate(c)

d = calculate_private_key(n, p)

print("Encryption broken in {} s\n".format(float(time.time() - time1)))
print("Decrypted message: {}".format(custom_decrypt(n, d, encrypted.ciphertext)))

