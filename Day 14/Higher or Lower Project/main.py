import random

import art
from game_data import data
from art import logo
from art import vs
def get_random_account():
    """Get a random account dictionary from data."""
    return random.choice(data)

def format_data(account):
    """Format account data into printable text."""
    name = account["name"]
    description = account["description"]
    country = account["country"]
    return f"{name}, a {description}, from {country}."

def check_answer(guess, a_followers, b_followers):
    """Check if the user's guess matches the account with higher followers."""
    if a_followers > b_followers:
        return guess == "a"
    else:
        return guess == "b"

def play_game():
    print(logo)
    score = 0
    game_should_continue = True
    account_a = get_random_account()
    account_b = get_random_account()

    while game_should_continue:
        # Prevent account_a and account_b from being identical
        while account_a == account_b:
            account_b = get_random_account()

        print(f"Compare A: {format_data(account_a)}.")
        print(vs)
        print(f"Against B: {format_data(account_b)}.")

        guess = input("Who has more followers? Type 'A' or 'B': ").lower()

        # Input validation
        while guess not in ["a", "b"]:
            guess = input("Invalid choice. Type 'A' or 'B': ").lower()

        a_follower_count = account_a["follower_count"]
        b_follower_count = account_b["follower_count"]

        is_correct = check_answer(guess, a_follower_count, b_follower_count)

        if is_correct:
            score += 1
            print(f"You're right! Current score: {score}.\n")
            # Account B becomes Account A for the next round
            account_a = account_b
            account_b = get_random_account()
        else:
            game_should_continue = False
            print(f"Sorry, that's wrong. Final score: {score}")

# Start the game
play_game()