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

def deal_cards():
    hand = []
    
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
    deal_cards()   