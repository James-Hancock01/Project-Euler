##Champernowne's Constant
from functools import reduce
from tqdm import tqdm as tqdm
dec = '0'
n = 1
with tqdm(total = 1000000, desc = 'Creating number') as pbar:
    while len(dec) <= 1000000:
        dec += str(n)
        pbar.update(n)
        n += 1
    pbar.close()

print(reduce((lambda x, y: x*y), [int(dec[10**i]) for i in range(0,7)]))
