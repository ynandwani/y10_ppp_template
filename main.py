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
    card_1 = randint[(0,len(deck) - 1)]
    if card_1 == 'king' or card_1 == 'queen' or card_1 == 'jack':
        card_1 = 10
    elif card_1 =='ace':
        card_1 = 11
        hand.append(deck[card_1])
        deck.remove[card_1]
    else:
        hand.append(deck[card_1])
    
    if card_2 == 'king' or card_2 == 'queen' or card_2 == 'jack':
        card_2 = 10
    elif card_2 =='ace':
        card_2 = 11
        hand.append(deck[card_2])
        deck.remove[card_2]
    else:
        hand.append(deck[card_2])


    print(f"Your hand is: {hand}")

    return hand, card_1, card_2

def count_cards(hand):
    hand_total = 0
    index = 0
    for i in range(len[hand] - 1):
            hand_total += hand(index) 
            index += 1
    if 11 in hand and hand_total > 10:
        hand -= 10

    print(f"Your total is: {hand_total}.")

    if len(hand) == 2:
        if hand[0] == hand[1]:
            split = input("Do you want to split your hand?").lower()
            if split == "yes":
                split()
            else:
                hand_next()
            
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
    card = deck[randint(0,len(deck) - 1)]

    if card == 11 and hand_total > 10:
        card = 1
    
    hand_total = hand_total + card
    if card == 'king' or card == 'queen' or card == 'jack':
        card = 10
    elif card =='ace':
        card = 11
        hand_total = hand_total + card
        deck.remove[card]
    else:
        hand_total = hand_total + card
    hand_next()
    
    

def stand(hand_total):
    print(f"Your hand is: {hand_total}")


def double_down():
    pass

def split():
    pass

def dealer_deal_cards():
    pass

def dealer_hit_or_stand():
    pass

def start():
    cards()
    deal_cards_start() 
    count_cards()
    hand_next()
    #save
 
