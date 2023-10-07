import time

Whole_Deck = []

def FillDeck(Deck):
    for i in range(1,53):
        Deck.append(i)

def splitDeck(Deck):
    NewDeck = []
    halfDeckMark = 26
    for i in range(0, halfDeckMark):
        NewDeck.append(Deck[i])
        NewDeck.append(Deck[i + halfDeckMark])
    return NewDeck

def DeckCheck(Deck):
    inOrder = True
    for i in range(0, 51):
        if Deck[i] >= Deck[i+1]:
            inOrder = False
    return inOrder

FillDeck(Whole_Deck)
print(Whole_Deck)

Whole_Deck = splitDeck(Whole_Deck)
count = 1

while not DeckCheck(Whole_Deck):
    count += 1
    Whole_Deck = splitDeck(Whole_Deck)
    # print(Whole_Deck)


print("Count: ", count)
print(Whole_Deck)
