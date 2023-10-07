from tqdm import tqdm as tqdm

#n = list(dict.fromkeys([''.join(sorted([str(142857*mult) for mult in range(1,7)], key = str(1234567890).index)]))
#Orders values of string numerically removing duplicates
#print(''.join(sorted(set(str(n1)), key = str(1234567890).index)) == ''.join(sorted(set(str(n1*2)), key = str(1234567890).index)))


found = False
n = 1
max = 6



with tqdm(initial = n, total = max, desc = 'Finding permuted multiples') as pbar:
    while found == False:
        n += 1
        nums = list(dict.fromkeys([''.join(sorted(str(n*mult), key = str(1234567890).index)) for mult in range(1,max+1)]))
        pbar.n = max-len(nums)+1
        if n % 10000 == 0: pbar.set_description("Processing %s" %n)
        pbar.refresh()
        if len(nums) == 1:
            found = True

print(n)
print('\n', [n * mult for mult in range(1, max+1)])
