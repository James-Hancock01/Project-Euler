import csv
from itertools import product
from string import ascii_lowercase, ascii_letters,digits, punctuation
import string
import re
keywords = map(''.join, product(ascii_lowercase, repeat=3))


cipher = ''.join(map(chr,[(int(x)) for x in open('./files/p059_cipher.txt').read().strip().split(',')]))
#print(cipher)

def decrypt(plaintext: str, key: str) -> str:
	decrypted = ""
	for i in range(len(plaintext)):
		#print('{0} ^ {1}'.format(plaintext[i], key[i%3]))
		decrypted += (chr(ord(plaintext[i]) ^ ord(key[i%len(key)])))
	return decrypted

def checkchars(txt: str)-> bool:
	return all((True if x in ascii_letters + digits + punctuation + ' '  else False for x in txt))

def checkwords(txt: str)-> bool:
	substrings = ['an', 'and', 'in', 'of', 'at', 'to']	#using the fact the text is in english
	if all(re.search(r'\b{0}\b'.format(substring), txt) for substring in substrings): return True	#regex to detect if the substrings are in the text
	return False

def findsumofascii(txt: str)-> int:
	for i in txt[:10]:
		return sum([ord(i) for i in txt])

for key in keywords:
	txt = decrypt(cipher, key)
	if checkchars(txt):
		if checkwords(txt):
			print('key: ', key)
			print(txt)
			print(findsumofascii(txt))




print(checkwords('^l%zzqmc and in fk"q~i`q"cmm'))
