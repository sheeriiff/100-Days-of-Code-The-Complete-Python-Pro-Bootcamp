import random
numbers = ['w', 'e', 'e', 'r', 'f', 'v', 'i', 'a', 'w', 'k']
password = ""
for char in numbers:
    password += random.choice(numbers)
print(password)
