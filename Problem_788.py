#Dominating numbers
from collections import Counter
from tqdm import tqdm as tqdm
from tqdm import trange
from time import sleep
def d(N: int)-> int:
	return count_dom_nums(10**N)

def count_dom_nums(limit: int, min: int = 1):
	count = 0
	for i in tqdm(range(min, limit)):
		res = Counter(str(i))
		res = max(res, key = res.get)
		if 2 * str(i).count(res) > len(str(i)): count += 1
	return count

print(d(10))
