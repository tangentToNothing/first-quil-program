import math
import sys
import random
from random import choice
from primesieve import *
import bisect

MAX_BIT_SIZE = 32

def eratosthenes(bit_length):
    '''Yields the sequence of prime numbers via the Sieve of Eratosthenes.'''
    D = {}  # map composite integers to primes witnessing their compositeness
    q = 2
    while 1:
        if q not in D:
            if q.bit_length() < bit_length:
                pass
            elif q.bit_length() > bit_length:
                break
            else:
                yield q        # not marked composite, must be prime
            D[q*q] = [q]   # first multiple of q not already marked
        else:
            for p in D[q]: # move each witness to its next multiple
                D.setdefault(p+q,[]).append(p)
            del D[q]       # no longer need D[q], free memory
        q += 1

def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

def multiplicative_inverse(e, phi):
    d = 0
    x1 = 0
    x2 = 1
    y1 = 1
    temp_phi = phi
    
    while e > 0:
        temp1 = temp_phi // e
        temp2 = temp_phi - (temp1 * e)
        temp_phi = e
        e = temp2
        
        x = x2 - (temp1 * x1)
        y = d - (temp1 * y1)
        
        x2 = x1
        x1 = x
        d = y1
        y1 = y
    
    if temp_phi == 1:
        return d + phi


class PublicKey:

    def __init__(self, n, e):
        self.e = e
        self.n = n

    def encrypt(self, message):
        cipher = [pow(ord(char), self.e, self.n) for char in message]
        return CipherText(cipher)

class PrivateKey:

    def __init__(self, n, d):
        self.d = d
        self.n = n

    def decrypt(self, ciphertext):
        decrypted = [chr(pow(char, self.d, self.n)) for char in ciphertext]
        return ''.join(decrypted)

class CipherText:

    def __init__(self, cipher_text):
        self.ciphertext = cipher_text

    def __str__(self):
        return ''.join(map(lambda x: str(x), self.ciphertext))

class KeyPair:

    def __init__(self, bits):
        if bits > MAX_BIT_SIZE:
            print("There is no way we can crack RSA of {} bits right now. \nToo lazy.".format(MAX_BIT_SIZE))
            sys.exit(0)
        prime_list = primes(1, 2**bits)
        small_primes = prime_list[bisect.bisect_left(prime_list, 2**(bits-1) -1):]
        #small_primes = [_ for _ in eratosthenes(bits)]
        p = choice(small_primes)
        small_primes.remove(p)
        q = choice(small_primes)

        n = p * q
        phi = (p-1) * (q-1)

        e = random.randrange(1, phi)

        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(1, phi)
            g = gcd(e, phi)

        d = multiplicative_inverse(e, phi)
        self.publickey = PublicKey(n, e)
        self.privatekey = PrivateKey(n, d)

