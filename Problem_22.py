import string
import csv


alphabet = string.ascii_lowercase   #value will come from the index of the letter + 1

def nameScore(name:string, index:int)-> int:   #converts the name into the sum of its letters
    wordSum = 0
    for letter in name:
        wordSum += alphabet.index(letter.lower())+1
    return wordSum*(index+1)




with open("./files/Problem22Names.txt","r") as file:
    names = []
    csv_reader = csv.reader(file, delimiter = ',')
    for row in csv_reader:
        for item in row:
            names.append(item)
    file.close()

names.sort()
total = 0
for name in names:
    total += nameScore(name, names.index(name))

print(("The total of every name in the file is {0}").format(total))
