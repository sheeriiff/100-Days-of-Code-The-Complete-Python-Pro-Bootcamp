print(r'''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\ ` . "-._ /_______________|_______
|                   | |o ;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

direction = input("left or right? ").lower()
if direction == "left" or direction == "Left":
    swimming = input("Swim or wait for a boat? ")
    if swimming == "wait" or swimming == "Wait":
        door = input("Which door? Blue or Red or Yellow: ")
        if door == "red" or door == "Red":
            print("Game Over...you were burned by fire.")
        elif door == "blue" or door == "Blue":
            print("Game Over...you were eaten by beasts.")
        elif door == "yellow" or door == "Yellow":
            print("Congratulations! you found the treasure.")
        else:
            print("Game Over")
    elif swimming == "swim":
        print("you sank")
    else:
        print("You typed the wrong inputs.")
elif direction == "right" or direction == "Right":
    print("Fall into a hole.")
else:
    print("You typed the wrong inputs.")

