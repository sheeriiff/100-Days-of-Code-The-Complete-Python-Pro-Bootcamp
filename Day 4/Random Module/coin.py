import random

n = 100000   # number of flips

# probabilities
P_head_biased = 0.37
P_head_fair = 0.5

biased_results = []
fair_results = []

for _ in range(n):
    # biased coin
    if random.random() < P_head_biased:
        biased_results.append(1)
    else:
        biased_results.append(0)

    # fair coin
    if random.random() < P_head_fair:
        fair_results.append(1)
    else:
        fair_results.append(0)

# averages
biased_average = sum(biased_results) / n
fair_average = sum(fair_results) / n

print("Biased coin average:", biased_average)
print("Fair coin average:", fair_average)