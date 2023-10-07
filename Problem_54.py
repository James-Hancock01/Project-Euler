# Poker Hands
import csv
import time
from tqdm import tqdm as tqdm

possiblehands = {#All possible hands with a value allocated. Total hand value = value + highest card
    'High Card': 0 ,
    'One Pair': 1000,
    'Two Pairs': 2000,
    'Three of a kind':3000,
    'Straight':4000,
    'Flush':5000,
    'Full House':6000,
    'Four of a kind':7000,
    'Straight Flush':8000,
    'Royal Flush':9000}
suits = {
    'S':'Spades',
    'H':'Hearts',
    'D':'Diamonds',
    'C':'Clubs'
}
numbers = {
    '1':1,
    '2':2,
    '3':3,
    '4':4,
    '5':5,
    '6':6,
    '7':7,
    '8':8,
    '9':9,
    'T':10,
    'J':11,
    'Q':12,
    'K':13,
    'A':14
}

class Card:
    def __init__(self, number:str, suit:str):
        self.suit = suits[suit]
        self.number = numbers[number]

    def number(self):
        return self.number

    def suit(self):
        return self.suit

    def readCard(self):
        print(("{0} of {1}").format(self.number, self.suit))

class Poker:
    def __init__(self):
        self.active = True

    def gameEnd():
        self.active = False

    def isStraight(self, hand):
        if hand[0].number == 14 and hand[4].number == 2 and hand[3].number == 3 and hand[2].number == 4 and hand[1].number == 5:    #catch case Ace is low
            hand[0].number = 1
            return True
        for i in range(0,4):    #there are 5 cards
            if hand[i].number - hand[i+1].number != 1: return False
        return True

    def isSuited(self, hand: [Card]):
        for card in hand:
            if card.suit != hand[0].suit: return False
        return True

    def handValue(self, hand):
        hand.sort(key = Card.number, reverse = True)
        numbers = dict.fromkeys((x for x in range(2,15)), 0)
        #print("is straight: ", self.isSuited(hand))
        #print("is suited: ", self.isStraight(hand))
        if self.isStraight(hand) and self.isSuited(hand):
            print(hand[0].number)
            if hand[0].number== 14:
                print(("hand value is a {0}").format(possiblehands['Royal Flush']))
                return possiblehands['Royal Flush']
            return possiblehands['Straight Flush'] + hand[0].number

        if self.isSuited(hand): return possiblehands['Flush'] + hand[0].number
        if self.isStraight(hand): return possiblehands['Straight'] + hand[0].number

        for card in hand:
            numbers[card.number] += 1
        fourOfAKind = 0
        triples = 0
        pairs = 0
        for num in numbers:
            if numbers[num]==2: pairs += 1
            if numbers[num]==3: triples += 1
            if numbers[num]==4: fourOfAKind +=1

        #print(("pairs {0}, triples: {1}, fourOfAKind: {2}").format(pairs, triples, fourOfAKind))
        if fourOfAKind == 1: return possiblehands['Four of a kind'] + self.findPairs(numbers, 4) + self.finddHighCard(numbers)
        if pairs == 1 and triples == 1: return possiblehands['Full House'] + self.fullHighCard(numbers)
        if triples == 1: return possiblehands['Three of a kind'] + self.findPairs(numbers, 3) + self.findHighCard(numbers)
        if pairs == 2: return possiblehands['Two Pairs'] + self.findPairs(numbers, 2) + self.findHighCard(numbers)
        if pairs == 1: return possiblehands['One Pair'] + self.findPairs(numbers, 2) + self.findHighCard(numbers)
        return hand[0].number

    def findHighCard(self, numbers):
        #numbers is a dict:
        for i in range(14, -1, -1):
            if numbers[i] == 1: return i

    def fullHighCard(self, numbers):
        for i in range(14, -1, -1):
            if numbers[i] == 3: return i

    def findPairs(self, numbers, value):
        score = 0
        #print(numbers)
        for i in range(14, 1, -1):
            if numbers[i] == value:
                score += i
                #print('score + ', i, score)
                if value != 2: return score*14
                if score == i:
                    score *=14
                #print('score * 10', score)
        #print(score + possiblehands['Two Pairs'] + self.findHighCard(numbers), numbers)
        return score

#C1 = [Card('9','H'), Card('6','C'), Card('4','H'), Card('5','H'), Card('7','H')]


#C1.sort(key = Card.number, reverse = True)

#print(Game.isStraight(C1))
#print(Game.handValue(C1))
Game = Poker()
P1score = 0
P2score = 0
with open('./files/Problem54.txt','r') as file:
    names = []
    csv_reader = csv.reader(file, delimiter = ' ')
    with tqdm(total = 1000, desc = 'Playing hands') as pbar:
        for row in csv_reader:
            P1 = []
            P2 = []
            for i in range(0,5):
                P1.append(row[i])
                P2.append(row[i+5])
            H1 = []
            H2 = []
            for card in P1:
                H1.append(Card(card[0], card[1]))
            for card in P2:
                H2.append(Card(card[0], card[1]))
            P1Value = Game.handValue(H1)
            P2Value = Game.handValue(H2)
            #print(("P1 has {0}, P2 has {1}").format(P1Value, P2Value))
            if P1Value > P2Value:     #told each hand has a winner...
                P1score += 1
                #print("P1 wins: ", P1Value, P2Value)
            elif P1Value < P2Value:
                P2score += 1
                #print("P2 wins: ", P1Value, P2Value)
            else:
                print("draw", P1Value, P2Value)
                print(P1, P2)
                print(Game.handValue(H1), Game.handValue(H2))
                time.sleep(0.5)
                test = input("")
            pbar.update(1)
            #text = input("")
    file.close()

print("Player 1: ", P1score)
print("Player 2: ", P2score)
