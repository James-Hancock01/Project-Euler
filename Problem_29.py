ValueArray = []
n = 100
for a in range(2, n+1):
    for b in range(2,n+1):
        ValueArray.append(pow(a,b))
KeyedArray = list(dict.fromkeys(ValueArray))
print(len(KeyedArray))
