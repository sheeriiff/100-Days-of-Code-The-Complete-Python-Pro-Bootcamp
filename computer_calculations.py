import random

def dealer_calculations(cards, dealer_cards, current_score_dealer):
    if not current_score_dealer >= 18:
        extra_card_dealer = random.choice(cards)
        dealer_cards.append(extra_card_dealer)
        current_score_dealer += extra_card_dealer
    elif current_score_dealer >= 11 and 11 in dealer_cards:
        current_score_dealer -= 10
    else:
        current_score_dealer = dealer_cards[0] + dealer_cards[1]

    return current_score_dealer