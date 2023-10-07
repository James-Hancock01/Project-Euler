def factorial(n):
    n_fact = 1
    if n > 0:
        n_fact = factorial(n-1)
        n_fact *= n
    return n_fact

def splitToarray(n):
    individualNumbers = []
    word = str(n)
    for i in range(0, len(word)):
        individualNumbers.append(int(word[i]))
    return individualNumbers

def sumarray(ar):
    total = 0
    for i in ar:
        total += i
    return total

bigNumber = factorial(100)
splitarray = splitToarray(bigNumber)
sumofarray = sumarray(splitarray)

print(sumofarray)
