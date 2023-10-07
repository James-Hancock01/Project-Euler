import csv

def solve(tri):
    tri = list(tri)
    while len(tri) > 1:
        t0 = tri.pop()
        t1 = tri.pop()
        tri.append([max(t0[i], t0[i+1]) + t for i,t in enumerate(t1)])
    return tri[0][0]

with open('./files/Problem_67.txt','r') as file:
    data = """"""
    csv_reader = csv.reader(file, delimiter = ' ')
    for line in csv_reader:
        for item in line:
            data += item + ' '
        data += '\n'

    print(solve(list(map(int, row.split())) for row in data.splitlines()))  #map(int, ) filters to just integers
