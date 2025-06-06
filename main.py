# testing
from random import randint
from time import sleep

print("Revision Blackjack")

def cards():
    deck = []
    for i in range(10):
        for i in range(4):
            deck.append(i + 1)
    for i in range(4):
        deck.append('king','queen','jack','ace')
    
    return deck

def deal_cards_start(deck):
    hand = []
    card = ''
    for i in range(2):
        rand_index = random.randint(0,len(deck) - 1)
       card = hand.append(deck[rand_index])
    print(hand)
    return hand
    pass

def count_cards():
    pass

def hit_or_stand():
    pass

def double_down():
    pass

def split():
    pass

def print_cards():
    pass

def dealer_hit_or_stand():
    pass

def start():
    cards()
    deal_cards_start()  
