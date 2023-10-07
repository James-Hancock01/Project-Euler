#Digit fifth powers
from tqdm import tqdm as tqdm
power = 5
end = (9**power)*power
numbers = [True]*(end +1)

def isNthPower(num, pow):
    if num == 0: return False
    if num == 1: return False
    sum = 0
    for n in str(num):
        sum += int(n)**pow
    if sum == num: return True
    return False

def findDigitPowers(nums, pow):
    for i in tqdm(range(0, len(nums)), desc = ('Finding {0}th digit powers').format(pow)):
        numbers[i] *= isNthPower(i, power)
        #print(i, isNthPower(i, power))
    return [i for i in range(0, len(nums)) if nums[i]]

print(('The sum of the {0}th digit powers is {1}').format(power,sum(findDigitPowers(numbers, power))))
