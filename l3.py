print(" Welcome my Program \n\n")

# Custom exceptions to manage flow control without if/else statements
class InvalidChoice(Exception): pass
class BreakLoop(Exception): pass

def run_program_1(my_fn, my_ln):
    print("Program 1: \n")
    msg = f"{my_fn} {my_ln}"
    b = msg.encode()
    print(f"1. Bytes object: {b}")
    print(f"2. Bytes to string: {b.decode()}")
    print(f"3. Bytes to hex: {b.hex()}")
    print(f"4. Hex to bytes: {bytes.fromhex(b.hex())}")
    print(f"5. New bytearray: {bytearray(msg, 'utf-8')}")
    ba = bytearray(b)
    print(f"6. Bytes to bytearray: {ba}")
    
    # If space_index is -1, -1 + 1 becomes 0, returning b[0:] (the full string) without if-else
    space_index = msg.find(" ")
    sliced_b = b[space_index + 1:]
    print(f"7. Sliced bytes: {sliced_b}")
    
    # Replaced if-else check with try/except to guard empty inputs
    try:
        ba[0] = ord(my_fn[0].lower())
    except IndexError:
        pass
    print(f"8. Modified message: {ba.decode()}")

def run_program_2(my_fn, my_ln):
    print("\nProgram 2: ")
    print(f"\nFirst name: {my_fn}\nLast name: {my_ln}")
    
    full_name = f"{my_fn} {my_ln}"
    print(f"Full name: {full_name}")
    print(f"First character: {full_name[0]}")
    print(f"Last character: {full_name[-1]}")
    
    try:
        full_name[0] = "D"
    except TypeError:
        print("Strings are immutable; individual characters\ncannot be changed directly.")
        
    print(f"New name: D{my_fn[1:]}\nOriginal name: {my_fn}\nCharacters in the full name:")
    for char in full_name:
        print(char)
        
    print(f"Sliced first name: {my_fn}\nSliced last name: {my_ln}")
    
    search = input("Enter one character to search: ")
    idx = full_name.find(search)
    
    # Replaced if-else lookups with dictionary mapping
    search_results = {-1: "Character not found"}
    print(search_results.get(idx, f"Character found at index: {idx}"))
    print(f'The blank line between a and S is the space in "{my_fn} {my_ln}".')

def handle_invalid(*args):
    print("\nInvalid input! Please select a correct program number (1 or 2).")
    raise InvalidChoice

# Dictionary routing to pick the chosen application branch
program_menu = {
    "1": run_program_1,
    "2": run_program_2
}

# Functions to handle continuation choices without conditional statements
def choose_yes():
    raise BreakLoop

def choose_no():
    print("\nProgram Terminated! Thanks for using my program :)")
    exit()

def choose_invalid():
    print("Invalid input. Please type Y or N.")

continuation_menu = {
    "Y": choose_yes,
    "N": choose_no
}

# Main Application Loop
while True:
    my_fn = input("Enter your First Name: ")
    my_ln = input("Enter your Last Name: ")
    print("Select program you want to run\n")
    print("1. Run Program 1: Bytes and Bytearray")
    print("2. Run Program 2: Name immutable")

    choice = input("\nChoice what program you want to run: ")

    try:
        # Route to program or trigger the error handler directly
        program_menu.get(choice, handle_invalid)(my_fn, my_ln)
    except InvalidChoice:
        continue

    # Continuation Prompter Loop
    while True:
        run_again = input("\nDo you want to continue (Y/N)? ").strip().upper()
        try:
            # Map choice directly to operations, defaulting to the error handler function
            continuation_menu.get(run_again, choose_invalid)()
        except BreakLoop:
            break




