from random import randint
from time import sleep
import os

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
    print(f"{player} split the hand.")
    hand_1 = [hand[0], deck.pop(randint(0, len(deck) - 1))]
    hand_2 = [hand[1], deck.pop(randint(0, len(deck) - 1))]
    
    print(f"{player}'s hands after split: {hand_1} and {hand_2}")
    
    return hand_1, hand_2, deck

def player_bust():
    print("You busted! Dealer wins.")

def dealer_bust():
    print("Dealer busted! You win.")

def who_won(dealer_hand_total, hand_total, bet):
    if hand_total > 21:
        print("You busted! Dealer wins.")
        return -bet
    elif dealer_hand_total > 21:
        print("Dealer busted! You win.")
        return bet
    elif hand_total > dealer_hand_total:
        print("You win!")
        return bet
    elif hand_total < dealer_hand_total:
        print("Dealer wins!")
        return -bet
    else:
        print("It's a tie.")
        return 0

def betting():
    num_questions = int(input("How many math questions do you want to answer to determine your bet? "))
    bet = 0
    for _ in range(num_questions):
        num1 = randint(1, 10)
        num2 = randint(1, 10)
        correct_answer = num1 + num2
        answer = int(input(f"What is the sum of {num1} and {num2}? "))
        if answer == correct_answer:
            bet += 1
        else:
            break
    return bet

def start():
    balance = 100
    play = input("Press Y to play. Otherwise, press N.").lower()
    while play == 'y' and balance > 0:
        bet = betting()
        deck = cards()
        player_hand, deck = deal_cards_start(deck)
        dealer_hand = []

        player_total = count_cards(player_hand, "You")
        
        while player_total <= 21:
            action = input("Do you want to hit, stand, double down, or split? (hit/stand/double/split)").lower()
            if action == 'hit':
                player_hand, deck = hit(player_hand, deck, "You")
                player_total = count_cards(player_hand, "You")
            elif action == 'stand':
                break
            elif action == 'double':
                player_hand, deck = double_down(player_hand, deck, "You")
                player_total = count_cards(player_hand, "You")
                bet *= 2
            elif action == 'split' and player_hand[0] == player_hand[1]:
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

        if player_total > 21:
            balance -= bet
        else:
            dealer_total = count_cards(dealer_hand, "Dealer")

            if player_total <= 21:
                while dealer_total < 17:
                    dealer_hand, deck = hit(dealer_hand, deck, "Dealer")
                    dealer_total = count_cards(dealer_hand, "Dealer")
                    if dealer_total > 21:
                        break

            balance += who_won(dealer_total, player_total, bet)

        print(f"Your balance: {balance}")
        play = input("Press Y to play again. Otherwise, press N.").lower()

    print("Game over! Thanks for playing.")

if __name__ == "__main__":
    start()