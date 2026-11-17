import art
print(art.logo)
# TODO-1: Ask the user for input
Auction = {}
continue_or_not = True
while continue_or_not:

    # TODO-2: Save data into dictionary {name: price}
    name = input("what is your name?: ")
    price  = int(input("How much do you bid?: $"))

    Auction[name] = price
    print(Auction)

    # TODO-3: Whether if new bids need to be added
    decision = input("Are there any other bidders? Type 'yes or 'no'. \n").lower()
    print("\n" * 20)

    if decision == "no".lower():
        continue_or_not = False

print(Auction)
best_key = max(Auction, key=Auction.get)
best_val = Auction[best_key]
print(f"THe winner is {best_key} with a bid of ${best_val}")

# TODO-4: Compare bids in dictionary


