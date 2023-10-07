from tqdm import tqdm as tqdm
n = 10000

pents = [int(i*(3*i-1)/2) for i in range(1, n+1)]

def isPent(n: int):
    if (24*n+1)**0.5 % 6 == 5: return True
    return False


with tqdm(total = len(pents)**2, desc = 'checking pents') as pbar:
    specialpents = []
    for i in pents:
        for j in pents:
            if i != j:
                if isPent(i+j):
                    if i-j > 0 and isPent(i-j):
                        specialpents.append(i-j)
            pbar.update(1)

print(specialpents)
print(min(specialpents))
