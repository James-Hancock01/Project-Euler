### Circular primes
import sys
sys.path.insert(0, 'C:/Users/jmcha/OneDrive/Documents/Atom/Maths')
import MathUtil as math
from tqdm import tqdm as tqdm
import time

max = 1000000
primes = math.PrimesToLimit(max)

def isCircular(p:int)-> bool:    #circulates the indices in the primes and checks if they are all Primes
    rotations = []
    for i in range(numberOfDigits(p)):
        rotations.append(int(leftRotate(str(p), i)))
    for n in rotations:
        if not n in primes: return False
    return True

def numberOfDigits(n: int) -> int:
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count

def leftRotate(s, d):
    tmp = s[d : ] + s[0 : d]
    return tmp

count = 0
circulars = []
with tqdm(total = len(primes), desc = "Finding Circular Primes") as pbar:
    for p in primes:
        pbar.update()
        if isCircular(p):
            circulars.append(p)
            count += 1
        #time.sleep(.001)
pbar.close()


print(("There are {0} circular primes under {1}").format(count,max))
