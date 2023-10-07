import sys
sys.path.insert(0, 'C:/Users/jmcha/OneDrive/Documents/Atom/Maths')
import MathUtil as mu
from tqdm import tqdm as tqdm

def isPandigital(n:int)-> bool:
    if n%9 != 0: return False   #pandigitals have to be divisible by 9
    n = ''.join(sorted(set(str(n)), key = str(n).index))
    return len(str(n)) == 10

def hasProperty(n:int, primes):
    if len(str(n)) < 10: return False
    for i in range(1, len(str(n)) - 2):
        num = int(str(n)[i:i+3])
        if num % primes[i-1] != 0: return False
    return True

primes = mu.PrimesToLimit(17)
sum = 0

print(primes[-1])
with tqdm(total = 9876543210 - 1234567890, desc = 'finding special pandigital numbers') as pbar:
    for i in range(1234567890, 9876543210, 1):     #pandigital numbers have to be divisible by 9 so can increase by 17*9 as the last 3 digits have to be divisible by 17
        if isPandigital(i):
            if hasProperty(i, primes):
                sum += i
        pbar.update(1)
    pbar.close()
print("The sum of all special pandigital numbers is ", sum)
