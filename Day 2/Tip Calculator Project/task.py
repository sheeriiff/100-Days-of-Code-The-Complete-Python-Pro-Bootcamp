print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("What percentage tip would you like to give? 10 12 15 "))
people = int(input("How many people to split the bill? "))

# print(round(bill * (1+tip/100) / int(people), 2))

final_bill = bill * (1+tip/100)
each_one = final_bill / people
clean_number = round(each_one, 2)
print(f"each person should pay: ${clean_number} ", )