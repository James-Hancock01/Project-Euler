##Square root convergents

"""fraction of form:
	 a
	---
	b+c
where c = a/b

"""
iterations = [(0,0)]

number = (1,2)

def src(num, it, fracs):
	if it == 0: return num

	return (num[0]*fracs[it][1], 2*fracs[it][1] + (fracs[it][0]-fracs[it][1]))

def proper_rational_num(num, a):
	return (num[1]*a+num[0], num[1])

def improper_len(frc):
	if len(str(frc[0]))> len(str(frc[1])): return True
	return False

for i in range(0,1000):
	term = proper_rational_num(src(number,i, iterations), 1)
	iterations.append(term)

count = 0
for ite in iterations:
	if improper_len(ite): count += 1

print(count)

#print(iterations[1:10])




