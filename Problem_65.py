##Convergence of e

"""Follows from problem 57
"""
iterations = [(0,0)]


iterable_e = [(2,2*(i//3 +1)) if i % 3 == 1 else (2,1) for i in range(0, 100)]
iterable_2 = [(1,2) for i in range(100)]
iterable_23 = [3 if i % 4 == 1 else 8 if i % 4 == 3 else 1 for i in range(0,100)]

number = [(2, i) for i in iterable_e]

def src(a, b, c, it, iterable = False, record: bool = False, datastore = [], inte = 1):
	if it == 0:	
		datastore.insert(0, inte)
		return 0
	f = c
	print(f)
	try:
		if iterable != False: f = iterable_2[it]
	except ex:
		print("No/Invalid iterable supplied:")
	# a / (b + c) where c = d/e
	if record == True: datastore.append(convert_to_proper(f, inte))

	return src(a,b,(a * f[1], b*f[1] + f[0]), it-1,iterable, record, datastore, inte)


def convert_to_proper(frac, integer):
	if frac == 0: return integer
	return (frac[1] * integer + frac[0], frac[1])

print(iterable_2[:5])
fracs = []
src(1, 2, (1,2), 4,False, True, fracs)
print(fracs)
