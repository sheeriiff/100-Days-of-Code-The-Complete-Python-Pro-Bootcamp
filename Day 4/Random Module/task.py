import random
from itertools import count

#
# random_integer = random.randint(12,24)
# print(random_integer)

# random_number_0_1 = random.random()
# print(round(random_number_0_1 , 2))
#
# random_float = random.uniform(3,4)
# print(random_float)

P_head = 0.37
biased_coin = random.random() # THIS INTERVAL DOES NOT INCLUDE 1
print(biased_coin)
if biased_coin <= P_head:
    print("head\n")
else:
    print("tail\n")

P_head_f = 0.5
fair_coin = random.random() # THIS DOES NOT INTERVAL INCLUDES 1
print(fair_coin)
if fair_coin <= P_head_f:
    print("head")
else:
    print("tail")

