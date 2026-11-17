import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
game_choices = [rock, paper, scissors]
user_decision = input("What do you choose? Rock, Papers, Scissors.\n").lower()
computer_decision = random.choice(game_choices)

if user_decision == "rock":
    print(game_choices[0])
    print("Computer Chose:", computer_decision)
elif user_decision == "paper":
    print(game_choices[1])
    print("Computer Chose:", computer_decision)
elif user_decision == "scissors":
    print(game_choices[2])
    print("Computer Chose:", computer_decision)
else:
    print("You typed the wrong inputs.")

if (user_decision == "rock" and computer_decision == game_choices[2]
        or user_decision == "scissors" and computer_decision == game_choices[1])\
        or user_decision == "paper" and computer_decision == game_choices[0]:
    print("You Win!")
elif (user_decision == "rock" and computer_decision == game_choices[1]
        or user_decision == "scissors" and computer_decision == game_choices[0])\
        or user_decision == "paper" and computer_decision == game_choices[2]:
    print("You lose!")
elif(user_decision == "rock" and computer_decision == game_choices[0]
        or user_decision == "scissors" and computer_decision == game_choices[2])\
        or user_decision == "paper" and computer_decision == game_choices[1]:
    print("It's a Draw")





