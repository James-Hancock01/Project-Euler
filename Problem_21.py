import sys
sys.path.insert(0, 'C:/Users/jmcha/OneDrive/Documents/Atom/Maths')
import MathUtil as mu
from tqdm import tqdm as tqdm

max = 10000
numbers = [sum(mu.divisors(i)) for i in tqdm(range(0, max + 1), desc = 'Generating divisor sums')]
sumAmicable = 0

def isProperDivisor(numbers, a, b):
    if a == b: return False
    if a == numbers[b]: return True
    return False

print(len(numbers))
with tqdm(total = len(numbers)-1, desc = 'Finding amicable numbers') as pbar:
    for i in range(1, len(numbers)):
        if numbers[i] < len(numbers) + 1:
            if isProperDivisor(numbers, i, numbers[i]):
                sumAmicable += i
        pbar.update(1)
    pbar.close()

print(('The sum of all amicable numbers under {0} is {1}').format(max,sumAmicable))
