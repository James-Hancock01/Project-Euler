'CODED TRIANGLE NUMBERS'
import math
import csv

def isTriangleNumber(tri: int)-> bool:
    n = math.sqrt(8*tri + 1)/2 -0.5
    if n == int(n): return True
    return False

def findWordValue(word: str)-> int:
    return sum([ord(char)-96 for char in word.lower()])


with open('./files/p042_words.txt', 'r') as file:
    csv_reader = csv.reader(file, delimiter = ',')
    for line in csv_reader:
            print(sum(isTriangleNumber(findWordValue(word)) for word in line))
