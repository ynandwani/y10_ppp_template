# testing

from random import randint
from time import sleep

print("Revision Blackjack")

def cards():
    deck = []
    for i in range(4):
        for i in range(10):
            deck.append(i + 1)
    for i in range(4):
        deck.append('king','queen','jack','ace')
    
    return deck

def deal_cards_start(deck):
    hand = []
    card_1 = ''
    card_2 = ''
    card_1 = random.randint(0,len(deck) - 1)
    if card_1 == 'king' or card == 'queen' or card == 'jack':
        card_1 = 10
    elif card_1 =='ace':
        card_1 = 11
        hand.append(deck[card_1])
        deck.remove[card_1]
    else:
        hand.append(deck[card_1])


    print(f"Your hand is: {hand}")
    return hand

def count_cards(hand):
    hand_total = 0
    index = 0
    for i in range(len[hand] - 1):
      hand_total += hand(index) 
      index += 1
    print(f"Your total is: {hand_total}.")
    return hand_total


def hand_next(hand_total):
    hit_or_stand = input(f"Your hand is: {hand_total}. Do you hit or stand?").lower()
    while hit_or_stand == 'hit':
            hit()
            hit_or_stand = input(f"Your hand is: {hand_total}. Do you hit or stand?").lower()
    if hit_or_stand == 'stand':
        stand()
    while hit_or_stand != 'hit' or  hit_or_stand != 'stand':
        print("Please try again:")
        hit_or_stand = input(f"Your hand is: {hand_total}. Do you hit or stand?").lower()
   
    return hit_or_stand 

def hit(hand_total, deck):
    

def stand():
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
    count_cards()
    hand_next()
 
 
