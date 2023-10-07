import sys
sys.path.insert(0, 'C:/Users/jmcha/OneDrive/Documents/Atom/Maths')
import MathUtil as mu
from tqdm import tqdm as tqdm

def findAbundants(max = 28124):
    Abnts= []
    for i in tqdm(range(1, max), desc='Finding abundants'):
        if sum(mu.divisors(i))>i:
            Abnts.append(i)
    return Abnts

max = 28124
abundants = findAbundants(max)

def CreateCombinations(abundants):
    allintegers = [True*x for x in range(1,max)]
    for i in tqdm(range(0, len(abundants)), desc = 'Creating all combinations'):
        for j in range(0, len(abundants)):
            #print(('{0} + {1} = {2}').format(abundants[i],abundants[j],abundants[i]+abundants[j]))
            if abundants[i] + abundants[j] <= len(allintegers):
                allintegers[abundants[i] + abundants[j]-1] *= False


    return [i + 1 for i in range(0, len(allintegers)) if allintegers[i]]
print(('The sum of all positive integers that cannot be written as the sum of two abundant numbers is {0}').format(sum(CreateCombinations(abundants))))
