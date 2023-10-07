prevLimit = 9
upperLimit = 33
Squares = []

def isPrime(n):
    if n == 2 or n == 3 or n==5: return True
    if n & 2 == 0 or n < 2: return False
    for i in range(3, int(n**0.5) + 1, 2):    #only odd numbers up to the sqrt of n
        if n % i == 0:
            return False
    return True

def populateDblSquares(ArrSqr):
    for n in range(1, int((0.5*upperLimit)**0.5)):    #dont need to go past the sqrt of upperlimit 0.5 bc doubling
        ArrSqr.append(2*n**2)
    return ArrSqr

def GoldbacksConjecture(n):
    for i  in range(0, int(n**0.5) - 1):
        #print("n - sq: ", n - Squares[i])
        if isPrime(n - Squares[i]):
            return True
    #print("False exit")
    return False

if isPrime(17):
    print("17 is prime")
else:
    print("its not prime")
Squares = populateDblSquares(Squares)
print(Squares)
TrueforOdd = True
n = prevLimit
for odd in range(prevLimit, upperLimit + 1, 2):   #upperLimit assumed
    if not isPrime(odd):
        TrueforOdd = GoldbacksConjecture(odd)
        n = odd
        #print("odd: ", n)
        #if TrueforOdd: print("TRUE")
        #if not TrueforOdd: print("False")
        if not TrueforOdd: break

if TrueforOdd:
    print("True: ", n)
else:
    print("False:", n)
