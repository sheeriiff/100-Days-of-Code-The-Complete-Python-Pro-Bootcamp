import art

def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations = { "+" : add,
               "-" : subtract,
               "*" : multiply,
               "/" : divide
               }

def calculator():
    print(art.logo)
    should_accumulate = True
    first_number = float(input("WHat's the first number: "))

    while should_accumulate:
        for sympol in operations:
            print(sympol)
        chosen_operation = input("Pick an operation:")
        second_number = float(input("What's the second number: "))

        answer = operations[chosen_operation](first_number, second_number)
        print(f"{first_number} {chosen_operation} {second_number} = {answer}")

        choice = input(f"type 'y' to continue calculating with {answer} or type 'n' to start a new calculation. ")

        if choice == "y":
            first_number = answer
        else:
            should_accumulate = False
            print("\n" * 20)
            calculator()

calculator()