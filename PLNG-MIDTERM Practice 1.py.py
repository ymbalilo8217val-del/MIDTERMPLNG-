while True:
    print()
    print("Choose the program you want to run")
    print("Program 1")
    print("Program 2")
    print("Program 3")
    print("Program 4")
    print("Program 5")
    print("Program 6")

    choice = input("Enter your choice (1-6): ").strip()

    if choice == "1":
        numbers = []
        print("Enter 10 real numbers (negative and positive):")
        for i in range(10):
            while True:
                try:
                    number = float(input("Element " + str(i + 1) + ": "))
                    numbers.append(number)
                    break
                except ValueError:
                    print("Invalid input. Please enter a number.")

        positive_sum = 0
        positive_count = 0
        negative_count = 0
        smallest = numbers[0]

        for number in numbers:
            if number > 0:
                positive_sum = positive_sum + number
                positive_count = positive_count + 1
            if number < 0:
                negative_count = negative_count + 1
            if number < smallest:
                smallest = number

        if positive_count > 0:
            print("Sum of positive numbers:", positive_sum)
            print("Average of positive numbers:", positive_sum / positive_count)
        else:
            print("No positive numbers were entered.")
        print("Count of negative numbers:", negative_count)
        print("Minimum value:", smallest)

    elif choice == "2":
        numbers = []
        print("Enter 8 integer numbers:")
        for i in range(8):
            while True:
                try:
                    number = int(input("Element " + str(i + 1) + ": "))
                    numbers.append(number)
                    break
                except ValueError:
                    print("Invalid input. Please enter an integer.")

        unique = []
        for number in numbers:
            if number not in unique:
                unique.append(number)
        print("Array without duplicates:", unique)

        unique.sort()
        if len(unique) >= 2:
            print("Second largest element:", unique[-2])
            print("Second smallest element:", unique[1])
        else:
            print("Not enough different numbers.")

    elif choice == "3":
        text = input("Enter data in array: ")
        try:
            numbers = []
            for part in text.split():
                numbers.append(int(part))

            print("Stored data in array:")
            for number in numbers:
                print(number, end=" ")
            print()

            position = int(input("Enter position of element to delete: "))
            if position >= 0 and position < len(numbers):
                numbers.pop(position)
                print("New data in array:")
                for number in numbers:
                    print(number, end=" ")
                print()
            else:
                print("Position", position, "is not in the array.")
        except ValueError:
            print("Invalid input.")

    elif choice == "4":
        try:
            size = int(input("Enter size of array: "))
            text = input("Enter " + str(size) + " elements: ")
            numbers = []
            for part in text.split():
                numbers.append(int(part))
            numbers = numbers[:size]

            print("Even elements:")
            for number in numbers:
                if number % 2 == 0:
                    print(number, end=" ")
            print()

            print("Odd elements:")
            for number in numbers:
                if number % 2 != 0:
                    print(number, end=" ")
            print()
        except ValueError:
            print("Please enter numbers only.")

    elif choice == "5":
        print("*")
        print("*A*")
        print("*A*A*")
        print("*A*A*A*")

    elif choice == "6":
        basic = 12000
        da = 0.12 * basic
        hra = 150
        ta = 120
        others = 450
        pf = 0.14 * basic
        income_tax = 0.15 * basic
        net = basic + da + hra + ta + others - pf - income_tax

        print("Basic Salary :", basic)
        print("DA           :", da)
        print("HRA          :", hra)
        print("TA           :", ta)
        print("Others       :", others)
        print("PF           :", pf)
        print("Income Tax   :", income_tax)
        print("------------------------")
        print("Net Salary   :", net)

    else:
        print("Invalid choice! Enter a number from 1 to 6.")
        continue

    again = input("Do you want to continue? Y/N: ").strip().upper()
    if again != "Y":
        print("Goodbye!")
        break