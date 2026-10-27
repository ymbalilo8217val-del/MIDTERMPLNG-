import random


def program_36():
    secret = random.randint(1, 100)
    tries = 0

    while True:
        text = input("Enter a number between 1 and 100 (0 to exit): ")

        if not text.isdigit():
            print("Invalid")
            continue

        number = int(text)

        if number == 0:
            print("You canceled the game.")
            break
        elif number > 100:
            print("Invalid")
        else:
            tries = tries + 1
            if number < secret:
                print("Enter a higher number.")
            elif number > secret:
                print("Enter a lower number.")
            else:
                print("The number was", secret)
                print("You guessed it in", tries, "tries")
                break


def program_45():
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            total = 0
            for digit in number:
                total = total + int(digit)
            print("Sum of the digits:", total)
            break
        else:
            print("Invalid")


def program_46():
    while True:
        number = input("Enter a number: ")
        if number.isdigit():
            result = 1
            for digit in number:
                if digit != "0":
                    result = result * int(digit)
            print("Product of the digits:", result)
            break
        else:
            print("Invalid")


def program_47():
    name = input("Enter a name: ")
    for i in range(10):
        print(name)


def program_50():
    total = 0
    while True:
        try:
            number = float(input("Enter a number (0 to stop): "))
        except ValueError:
            print("Invalid")
            continue
        if number == 0:
            break
        total = total + number
    print("Sum of the numbers:", total)


while True:
    choice = input("Enter program number (36, 45, 46, 47, 50, or q to quit): ")
    if choice == "q":
        break
    elif choice == "36":
        program_36()
    elif choice == "45":
        program_45()
    elif choice == "46":
        program_46()
    elif choice == "47":
        program_47()
    elif choice == "50":
        program_50()
    else:
        print("Invalid")