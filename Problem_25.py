def fibonnacci(a, b):
    c = a + b
    return c
n = 2
a = 1
b = 1

while True:

    temp = b
    b = fibonnacci(a, b)
    a = temp
    n += 1
    if len(str(b)) >= 1000:
        print(n,b)
        break

print(n)
