import sys
sys.path.insert(0, 'C:/Users/jmcha/OneDrive/Documents/Atom/Maths')
import MathUtil as mu
from tqdm import tqdm as tqdm

def NdistinctPrimeFactors(factorisation, noOfFactors: int) -> bool:
    if len(factorisation) == noOfFactors: return True
    return False

consecutive = 0
aim = 4
i = 0
consecutives = []

with tqdm(total = i, desc = 'Finding distinct primes') as pbar:
    while consecutive < aim:
        i += 1
        if NdistinctPrimeFactors(mu.PrimeFactorisation(i, False), aim):
            consecutive += 1
            consecutives.append(i)
        else:
            consecutive = 0
            consecutives = []
        pbar.update(1)
print(consecutives)
