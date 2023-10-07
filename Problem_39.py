import math

TrianglesbyP = []

for p in range(1, 1000): #note: smallest integer sided right angle triangle is 3,4,5 so perimeter 12
    solutions = []
    for a in range(1,math.ceil(p/2) + 1):   #side cannot be smaller than a third of the perimeter
        for b in range(a, math.ceil(p/2) + 1):
            c = p - a - b
            if c > p / 2: continue #means c is not the hypotenuse
            # print(a,b,c)
            if c == math.hypot(a,b): solutions.append((a,b,c))
        if c > p / 2: continue #means c is not the hypotenuse
    if len(solutions): TrianglesbyP.append([p] + [x for x in solutions])
##print(TrianglesbyP[:130])
targetIndex = 1
for i in range(0, len(TrianglesbyP)):
    # print(TrianglesbyP[i][0], len(TrianglesbyP[i]), TrianglesbyP[i])
    if len(TrianglesbyP[i]) > len(TrianglesbyP[targetIndex]): targetIndex = i

# print(TrianglesbyP[targetIndex][0], len(TrianglesbyP[targetIndex]))
print(TrianglesbyP[targetIndex])
print("DONE")
