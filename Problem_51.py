##Prime digit replacements
import sys
sys.path.insert(0, 'C:/Users/jmcha/OneDrive/Documents/Atom/Maths')
import MathUtil as mu
import math

def primesBetween(lower_limit = 10, upper_limit = math.inf):
	primes = mu.PrimesToLimit(100)
	for i in range(len(primes)):
		if primes[0] < lower_limit:
			primes.pop(0)
		else:
			for i in range(len(primes)):
				if primes[len(primes)-1]> upper_limit:
					primes.pop(len(primes)-1)
				else:
					return primes
	return primes

print(primesBetween())

def findfamilies(primes):
	for i in range(len(primes)):
		


