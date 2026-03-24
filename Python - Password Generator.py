import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the Password Generator!")
name = input("What is your name? \n").title()

app_continue = True

while app_continue:

    password = []

    nr_letters = int(input("How many letters would you like in your password?\n"))

    while nr_letters <= 0:
        print(f"Hmm…that doesn't look right. Enter a number above 0, {name}.")
        nr_letters = int(input("How many letters would you like in your password?\n"))

    nr_symbols = int(input(f"How many symbols would you like?\n"))
    nr_numbers = int(input(f"How many numbers would you like?\n"))

    for char in range(nr_letters):
        password += random.choice(letters)

    for char in range(nr_symbols):
        password += random.choice(symbols)

    for char in range(nr_numbers):
        password += random.choice(numbers)

    random.shuffle(password)
    password = "".join(password)

    print(f"{name}, your password is: {password}.")

    should_continue = input(f"Keep this password, {name} or create a new one? (y/n) \n").lower()

    if should_continue == "y":
        app_continue = True
    else:
        print(f"Thank you for using the password generator, {name}")
        app_continue = False