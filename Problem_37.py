##Truncatable Primes
import sys
import numpy
sys.path.insert(0, 'C:/Users/jmcha/OneDrive/Documents/Atom/Maths')
import MathUtil as mu
from tqdm import tqdm as tqdm


limit = 1000000
primes = mu.PrimesToLimit(limit, True)

def truncatablePrimeLeft(p: str)-> bool:
	if len(p) == 1: return False
	for i in range(len(p)):
		if not mu.isPrime(int(p[i:])): return False
	return True

def truncatablePrimeRight(p:str)-> bool:
	if len(p) == 1: return False
	for i in range(len(p)):
		if not mu.isPrime(int(p[:len(p)-i])): return False
	return True


print(truncatablePrimeLeft(str(3797)) and truncatablePrimeRight(str(3797)))

found = []
i = 0
with tqdm(total = 11, desc = 'truncatable primes found') as pbar:
	while len(found) < 11:
		if truncatablePrimeLeft(str(primes[i])) and truncatablePrimeRight(str(primes[i])):
			found.append(primes[i])
			pbar.update(1)
			#print(len(found), ": ", primes[i])
		i += 1
		if i > limit: 
			print("limit doubled")
			primes = mu.PrimesToLimit(2*limit, True)

print(sum(found))

