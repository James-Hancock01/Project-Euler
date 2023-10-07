#Goldbacks other conjecture

"""Conjecture: Every odd composite number can be written as the sum of a prime and twice a square"""

"""ALGORITHM:
1. Iterate through odd numbers (If prime then skip)
2. For odd numbers subtract square numbers and check if result is prime.
3. Find the case where the conjecture fails
"""

import sys
sys.path.insert(0, 'C:/Users/jmcha/OneDrive/Documents/Atom/Maths')
import MathUtil as mu
import math

def Goldbach(n, testn = False):
	if mu.isPrime(n): return True
	for i in range(1, math.floor(math.sqrt((n)/2))+1):
		if n == testn: print(n, i, n-2*(i**2))
		if mu.isPrime(n-2*(i**2)): return True
	return False

i = 3
while True:
	if not Goldbach(i): 
		print(i)
		exit()
	i += 2
