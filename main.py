from random import randint
from time import sleep
import os

text = "Welcome to Blackjack"
i = 0
for i in range(len(text)):
    print(text[i])
    sleep(0.05)
    

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

def player_bust():
    print("You busted! Dealer wins.")

def dealer_bust():
    print("Dealer busted! You win.")

def who_won(dealer_hand_total, hand_total):
    if hand_total > 21:
        player_bust()
    elif dealer_hand_total > 21:
        dealer_bust()
    elif hand_total > dealer_hand_total:
        print("You win!")
    elif hand_total < dealer_hand_total:
        print("Dealer wins!")
    else:
        print("It's a tie!")

def start():
    play = input("Press Y to play. Otherwise, press N.").lower()
    if play == 'y':
        deck = cards()
        player_hand, deck = deal_cards_start(deck)
        dealer_hand = []
        
        player_total = count_cards(player_hand, "You")
        
        while player_total <= 21:
            action = input("Do you want to hit, stand, or double down? (hit/stand/double)").lower()
            if action == 'hit':
                player_hand, deck = hit(player_hand, deck, "You")
                player_total = count_cards(player_hand, "You")
            elif action == 'stand':
                break
            elif action == 'double':
                player_hand, deck = double_down(player_hand, deck, "You")
                player_total = count_cards(player_hand, "You")
                break

        if player_total > 21:
            player_bust()
        else:
            dealer_total = count_cards(dealer_hand, "Dealer")

            if player_total <= 21:
                while dealer_total < 17:
                    dealer_hand, deck = hit(dealer_hand, deck, "Dealer")
                    dealer_total = count_cards(dealer_hand, "Dealer")
                    if dealer_total > 21:
                        break

            who_won(dealer_total, player_total)
    else:
        print("See you next time!")
        sleep(3)
        clear_terminal()

if __name__ == "__main__":
    start()
