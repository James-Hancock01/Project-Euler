"""COMBINATORIC SELECTIONS"""
import math
from tqdm import tqdm as tqdm


def Combination(n: int, r: int)-> int:
    if r == 0: return 1
    if r == 1: return r
    return math.factorial(n)/(math.factorial(r)*math.factorial(n-r))

print(Combination(5,3))


count = 0
for n in tqdm(range(1, 101), desc = 'Finding combinatoric selections > 1,000,000'):
    for r in range(0, n):
        if Combination(n, r)>1e6: count += 1

print(count)
