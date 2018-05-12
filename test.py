from pyquil.quil import Program 
from pyquil.api import QVMConnection 
from pyquil.gates import H, CNOT, MEASURE

import Crypto
from Crypto.PublicKey import RSA
from Crypto import Random
import ast

import time

from simplersa import eratosthenes
from primesieve import *
import bisect

#print(primes(2**30 - 1, 2**31 - 1))
time1 = time.time()
prime_list = primes(1, 2**32)
correct_list = prime_list[bisect.bisect_left(prime_list, 2**31 -1):]
print(correct_list[-1])
time_taken_primes = float(time.time() - time1)

time2 = time.time()
e_primes = [_ for _ in eratosthenes(20)]
print(e_primes[-1])
time_taken_e_primes = float(time.time() - time2)

print("Primesieve time taken: {}".format(time_taken_primes))
print("eratosthenes time taken: {}".format(time_taken_e_primes))




# qvm = QVMConnection() 
# p = Program(H(0), CNOT(0, 1), MEASURE(0, 0), MEASURE(1, 1)) 
# results = qvm.run(p, classical_addresses=[0, 1], trials=10)


