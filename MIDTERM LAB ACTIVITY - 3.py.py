message = "Hello Python"
first_name = "Maria"
last_name = "Santos"
full_name = first_name + " " + last_name

while True:
    program = input("Enter program number (1 for Bytes, 2 for Strings, q to quit): ")

    if program == "q":
        break

    if program != "1" and program != "2":
        print("Invalid")
        continue

    task = input("Enter task number (1 to 8): ")

    if task not in ["1", "2", "3", "4", "5", "6", "7", "8"]:
        print("Invalid")
        continue

    if program == "1":
        data = message.encode("utf-8")

        if task == "1":
            print(data)
        elif task == "2":
            print(data.decode("utf-8"))
        elif task == "3":
            print(data.hex())
        elif task == "4":
            hex_text = "48656c6c6f20507974686f6e"
            print(bytes.fromhex(hex_text))
        elif task == "5":
            print(bytearray("Hello Python", "utf-8"))
        elif task == "6":
            print(bytearray(data))
        elif task == "7":
            print(data[6:])
        elif task == "8":
            letters = bytearray(data)
            letters[0] = ord("h")
            print(letters.decode("utf-8"))

    elif program == "2":
        if task == "1":
            print("First name:", first_name)
            print("Last name:", last_name)
        elif task == "2":
            print("Full name:", full_name)
        elif task == "3":
            print("First character:", first_name[0])
            print("Last character:", last_name[-1])
        elif task == "4":
            try:
                first_name[0] = "D"
            except TypeError:
                print("Strings cannot be changed like this")
        elif task == "5":
            new_name = "D" + first_name[1:]
            print("New name:", new_name)
            print("Original name:", first_name)
        elif task == "6":
            for letter in full_name:
                print(letter)
        elif task == "7":
            print("First name:", full_name[0:5])
            print("Last name:", full_name[6:])
        elif task == "8":
            while True:
                letter = input("Enter one character to search: ")
                if len(letter) == 1:
                    if letter in full_name:
                        print("Found at index:", full_name.find(letter))
                    else:
                        print("Not found")
                    break
                else:
                    print("Invalid")