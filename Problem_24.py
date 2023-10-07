import itertools
array_nums = list(range(10))
temp = itertools.islice(itertools.permutations(array_nums), 999999, None)
print("".join(str(x) for x in next(temp)))
