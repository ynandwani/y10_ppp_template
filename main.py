from random import randint
import random
import os
from time import sleep
from sympy import Symbol, solve

welcome_message = "Welcome to Blackjack! "
i = 0
for i in range(len(welcome_message)):
    print(welcome_message[i], end = ' ') 
    i += 1
    sleep(0.1)
print('\n')

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def cards():
    deck = []
    for _ in range(4):
        for i in range(1, 11):
            deck.append(i)
    for _ in range(4):
        deck.extend([10, 10, 10, 'ace'])
    return deck

def deal_cards_start(deck):
    hand = []
    card_1 = deck.pop(randint(0, len(deck) - 1))
    card_2 = deck.pop(randint(0, len(deck) - 1))

    hand.append(card_1 if card_1 != 'ace' else 11)
    hand.append(card_2 if card_2 != 'ace' else 11)
    
    print(f"Your hand is: {hand}")
    return hand, deck

def count_cards(hand, player):
    hand_total = sum(hand)
    if 11 in hand and hand_total > 21:
        hand_total -= 10

    print(f"{player} total is: {hand_total}.")
    
    return hand_total

def hit(hand, deck, player):
    card = deck.pop(randint(0, len(deck) - 1))

    if card == 'ace' and sum(hand) + 11 <= 21:
        card = 11
    elif card == 'ace':
        card = 1

    hand.append(card)
    print(f"{player} drew: {card}")
    return hand, deck

def stand(hand_total):
    return hand_total

def double_down(hand, deck, player):
    card = deck.pop(randint(0, len(deck) - 1))

    if card == 'ace' and sum(hand) + 11 <= 21:
        card = 11
    elif card == 'ace':
        card = 1

    hand.append(card)
    print(f"{player} doubled down and drew: {card}")
    return hand, deck

def split_hand(hand, deck, player):
    if hand[0] == hand[1]:
        print(f"{player} split the hand.")
        hand_1 = [hand[0], deck.pop(randint(0, len(deck) - 1))]
        hand_2 = [hand[1], deck.pop(randint(0, len(deck) - 1))]
        
        print(f"{player}'s hands after split: {hand_1} and {hand_2}")
        return [hand_1], [hand_2], deck
    else:
        print("You can only split if you have a pair of cards with the same value.")
        return [hand], [], deck

def player_bust():
    print("You busted! Dealer wins.")

def dealer_bust():
    print("Dealer busted! You win.")

def who_won(dealer_hand_total, hand_total):
    if hand_total > 21:
        print("You busted! Dealer wins.")
        question()
    elif dealer_hand_total > 21:
        print("Dealer busted! You win.")
    elif hand_total > dealer_hand_total:
        print("You win!")
    elif hand_total < dealer_hand_total:
        print("Dealer wins!")
        #question()
    else:
        print("It's a tie.")

    play_again = input("Do you want to play again?(Y/N)").lower()
    if play_again =='y':
        clear_terminal()
        start()
    else:
        print("Ok, bye!")

#def question():
    #directory = r"C:\Users\ynandwani\OneDrive - Kellett School\PPP MATHS REVISION QUESTIONS FOR BLACKJACK"
    ##list the files
    #files = [f for f in os.listdir(directory)]
    #random_file = random.choice(files)
    #file_path = os.path.join(directory, random_file)
    
    # Open the random file
    #with open(file_path, 'r') as file:
        #content = file.read()
        #print(f"Contents of {random_file}:\n")
        #ans = input(f"SOLVE: {content}")
        #solution = solve(content)

    #while ans != solution:
        #print("Try again.")
        #ans = input(f"SOLVE: {content}")
        #give_answer = input("If you cannot solve it, press X to get the answer.").lower()
        #if give_answer == 'x':
            #print(f"The solution is: {solution}")
    #print("Great job!")


def start():

    deck = cards()
    player_hand, deck = deal_cards_start(deck)
    dealer_hand = []

    player_total = count_cards(player_hand, "You")
    
    while player_total <= 21:
        action = input("Do you want to hit, stand, double, or split? (hit/stand/double/split)").lower()
        if action == 'hit':
            player_hand, deck = hit(player_hand, deck, "You")
            player_total = count_cards(player_hand, "You")
        elif action == 'stand':
            break
        elif action == 'double':
            player_hand, deck = double_down(player_hand, deck, "You")
            player_total = count_cards(player_hand, "You")
        elif action == 'split':
            if player_hand[0] == player_hand[1]:
                hand_1, hand_2, deck = split_hand(player_hand, deck, "You")
                
                player_total_1 = count_cards(hand_1, "Hand 1")
                player_total_2 = count_cards(hand_2, "Hand 2")
                
                action_1 = input("Do you want to hit or stand on Hand 1? (hit/stand)").lower()
                while action_1 == 'hit' and player_total_1 <= 21:
                    hand_1, deck = hit(hand_1, deck, "Hand 1")
                    player_total_1 = count_cards(hand_1, "Hand 1")
                    action_1 = input("Do you want to hit or stand on Hand 1? (hit/stand)").lower()

                action_2 = input("Do you want to hit or stand on Hand 2? (hit/stand)").lower()
                while action_2 == 'hit' and player_total_2 <= 21:
                    hand_2, deck = hit(hand_2, deck, "Hand 2")
                    player_total_2 = count_cards(hand_2, "Hand 2")
                    action_2 = input("Do you want to hit or stand on Hand 2? (hit/stand)").lower()

                break
            else:
                print("You can only split if you have a pair of cards with the same value.")

    if player_total <= 21:
        dealer_total = count_cards(dealer_hand, "Dealer")

        while dealer_total < 17:
            dealer_hand, deck = hit(dealer_hand, deck, "Dealer")
            dealer_total = count_cards(dealer_hand, "Dealer")
            if dealer_total > 21:
                break

    who_won(dealer_total, player_total)

if __name__ == "__main__":
    start()