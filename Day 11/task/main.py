import random
from computer_calculations import dealer_calculations
from result import winner_decision
from art import logo

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

play_or_not = input("Do you want to play a game of Blackjack? Type \"y\" or \"n\": ")


user_cards = []
selected_cards_user = random.choices(cards, k = 2) #USER SELECTED CARDS
user_cards += selected_cards_user

dealer_cards = []
selected_cards_dealer = (random.choices(cards, k = 2))  #DEALER SELECTED CARDS
dealer_cards += selected_cards_dealer

current_score_user = user_cards[0] + user_cards[1]
current_score_dealer = dealer_cards[0] + dealer_cards[1]

print(f"Your cards: {user_cards}, Current score: {current_score_user}")
if current_score_user >= 11 and 11 in user_cards:
    current_score_user -= 10
print(f"Computer's first card: {dealer_cards[0]}\n")


add_again = True
while add_again:
    continue_or_pass = input("type \"y\" to get another card or \"n\" t pass: ")
    if continue_or_pass == "y":
        extra_card = random.choice(cards)
        user_cards.append(extra_card)
        current_score_user += extra_card
        print(f"Your cards: {user_cards}, Current score: {current_score_user}")
        if current_score_user >= 21:
            dealer_calculations(cards, dealer_cards, current_score_dealer)
            winner_decision(score_user = current_score_user, score_dealer = current_score_dealer,
                            computer_cards=dealer_cards)

    elif continue_or_pass == "n":
        dealer_calculations(cards, dealer_cards, current_score_dealer)
        winner_decision(score_user = current_score_user, score_dealer = current_score_dealer,
                        computer_cards = dealer_cards)
        add_again = False

# added a new comment

