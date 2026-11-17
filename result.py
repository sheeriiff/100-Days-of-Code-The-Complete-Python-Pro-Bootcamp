def winner_decision(score_user, score_dealer, computer_cards):
    if score_user == 21:
        print(f"computer cards {computer_cards}, score: {score_dealer}")
    elif score_dealer == 21:
        print(f"computer cards {computer_cards}, score: {score_dealer}")
        print("you lose")
    elif score_user > 21:
        print(f"computer cards {computer_cards}, score: {score_dealer}")
    elif score_user == score_dealer:
        print(f"computer cards {computer_cards}, score: {score_dealer}")
        print("Push")
    elif score_user > score_dealer and score_user <= 21:
        print(f"computer cards {computer_cards}, score: {score_dealer}")
        print("you win")
    elif score_user < score_dealer and score_dealer <= 21:
        print(f"computer cards {computer_cards}, score: {score_dealer}")
        print("you lose")