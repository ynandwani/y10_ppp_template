# testing

from random import randint
from time import sleep
import os

welcome = 'Revision Blackjack'
index = 0
for i in range(len(welcome)):
    print(welcome[index])
    index += 1
    sleep(0.2)

def cards():
    deck = []
    for i in range(4):
        for i in range(10):
            deck.append(i + 1)
    for i in range(4):
        deck.append('king','queen','jack','ace')
    
    return deck

def deal_cards_start(deck):
    hand = [[]]
    card_1 = ''
    card_2 = ''
    card_1 = randint[(0,len(deck) - 1)]
    if card_1 == 'king' or card_1 == 'queen' or card_1 == 'jack':
        card_1 = 10
    elif card_1 =='ace':
        card_1 = 11
        hand[0].append(deck[card_1])
        deck.remove[card_1]
    else:
        hand[0].append(deck[card_1])
    
    if card_2 == 'king' or card_2 == 'queen' or card_2 == 'jack':
        card_2 = 10
    elif card_2 =='ace':
        card_2 = 11
        hand[1].append(deck[card_2])
        deck.remove[card_2]
    else:
        hand[1].append(deck[card_2])


    print(f"Your hand is: {hand}")

    return hand, card_1, card_2

def dealer_deal_cards(hand, hand_total):
    deal_cards_start()
    dealer_hand = hand
    print(f"Dealer's first card is: {dealer_hand[0]}")
    count_cards()
    dealer_hand_total = hand_total
    
    
    return dealer_hand_total


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
    if hand_total < 22:
        hit_or_stand = input(f"Your hand is: {hand_total}. Do you hit or stand?").lower()
        if hit_or_stand == 'hit':
                hit()
                hit_or_stand = input(f"Your hand is: {hand_total}. Do you hit or stand?").lower()
        elif hit_or_stand == 'stand':
            stand()
        while hit_or_stand != 'hit' or  hit_or_stand != 'stand':
            print("Please try again:")
            hit_or_stand = input(f"Your hand is: {hand_total}. Do you hit or stand?").lower()
        
        return hit_or_stand 
    else:
        player_bust()
def hit(hand_total, deck):
    card = deck[randint(0, len(deck) - 1)]

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

def split(hand):
    hand_1 = hand[0]
    hand_2 = hand[1]
    return hand_1, hand_2

def hand_1(hand_1):
    hand_total = hand_1
    print(f"Your hand is: {hand_total}")
    hit()
    

def hand_2(hand_2):
    hand_total = hand_2
    print(f"Your hand is: {hand_total}")
    hit()

def player_bust():
    print("You busted!!! Dealer wins.")
    start()

def dealer_bust():
    print("Dealer busted!!! Player wins.")
    start()

def dealer_hit_or_stand(dealer_hand_total):
    if dealer_hand_total >= 17:
        dealer_stand()
    while dealer_hand_total < 17:
        dealer_hit()

def dealer_stand(dealer_hand_total):
    print(f"Dealer's hand is: {dealer_hand_total}")
    who_won()

def dealer_hit(dealer_hand_total, deck):
    card = deck[randint(0, len(deck) - 1)]

    if dealer_hand_total < 22:
        if card == 'king' or card == 'queen' or card == 'jack':
            card = 10
            dealer_hand_total = dealer_hand_total + card
            deck.remove[card]
        elif card =='ace':
            if dealer_hand_total > 10:
                card = 1
            if dealer_hand_total < 10:
                card = 11
            dealer_hand_total = dealer_hand_total + card
            deck.remove[card]
        else:
            dealer_hand_total = dealer_hand_total + card
        dealer_hit_or_stand()
    else:
        dealer_bust()

    return dealer_hand_total
    
def who_won(dealer_hand_total, hand_total):
    print(f"Player's hand is: {hand_total}")
    print(f"Dealer's hand is: {dealer_hand_total}")
    dealer = 21 - dealer_hand_total
    player = 21 - hand_total

    if player < dealer:
        print("Player won!")
        start()
    elif player > dealer:
        print("Dealer won!")
        start()
    else:
        print("Push!")
        start()

def clear_terminal():
    # For Windows
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

def start():
    play = input("Press Y to play. Otherwise, press N.").lower()
    if play == 'y':
        questions = 0
        cards()
        deal_cards_start()
        count_cards()
        dealer_deal_cards()
        hand_next()
        dealer_hit_or_stand()
        
    else:
        print("See you next time!")
        sleep(3)
        clear_terminal()
    
    
 
