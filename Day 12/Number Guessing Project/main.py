from random import randint
print("Welcome to the number guessing game!\n"
      "I'm thinking of a number between 1 and 100\n")
# random_number = random.choice(range(1, 101))
random_number = randint(1, 100)
print(random_number)

difficulty = str(input("choose a difficulty. Type 'easy' or 'hard': ").lower())
attempts = 0

def setting_difficulty(level):
    global attempts
    if level == "easy":
        attempts = 10
    elif level == "hard":
        attempts = 5
setting_difficulty(difficulty)

guessed_number = 0

def check_approaching(checked_number, exact_number):
    if checked_number >= exact_number+15:
        print("Too High")
    elif checked_number > exact_number and checked_number < exact_number+15:
        print("High")
    elif checked_number <= exact_number-15:
        print("Too Low")
    elif checked_number < exact_number and checked_number > exact_number-15:
        print("Low")


print(f"you have {attempts} attempts")

continue_guessing = True

while continue_guessing:
    guessed_number = int(input("make a guess: "))
    if guessed_number != random_number:
        check_approaching(checked_number=guessed_number, exact_number= random_number)
        attempts -= 1
        if attempts == 0:
            print("No attempts left")
            continue_guessing = False
            break
        print(f"you have {attempts} attempts left")
    elif guessed_number == random_number:
        print("Correct number")
        continue_guessing = False




