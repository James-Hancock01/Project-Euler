## Smallest multiple

def check(n, maxdivisor = 10):
    for i in range(maxdivisor, 1, -1):
        #print(("{0} mod {1} = {2}").format(n, i, n%i))
        if n % i != 0: return False
        if i == 2: return True
    return False

def findSmallestMultiple(multiples = 10, oldmax=1000, newmax=3000):
    print(("Searching for the smallest multiple of all numbers below {0} between {1} and {2}").format(multiples, oldmax, newmax))
    for n in range(oldmax, newmax+1, multiples):
        #print(n)
        if check(n, multiples):
            return n
            break
        if n == newmax:
            print("Finding new limit")
            return findSmallestMultiple(multiples, newmax, multiples*newmax)

print("Running")
multiples = 30
print(findSmallestMultiple(multiples, 30**3, 30**9))
print("End")
