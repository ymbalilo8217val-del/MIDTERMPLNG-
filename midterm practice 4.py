from datetime import date


def get_number(question):
    while True:
        text = input(question).strip()
        if text.isdigit():
            return int(text)
        print("Invalid input! Only numbers are allowed.")


def get_date(question):
    while True:
        text = input(question).strip()
        parts = text.split()
        if len(parts) != 3:
            print("Invalid format! Enter as MM DD YYYY (for example 08 15 2026).")
            continue
        try:
            month = int(parts[0])
            day = int(parts[1])
            year = int(parts[2])
            return date(year, month, day)
        except ValueError:
            print("Invalid date! Please try again.")


name = input("Enter your name: ").strip()
while True:
    only_letters = True
    for letter in name:
        if not letter.isalpha() and letter != " ":
            only_letters = False
    if name != "" and only_letters:
        break
    print("Invalid input! Name must contain only letters and spaces.")
    name = input("Enter your name: ").strip()

print("Welcome", name)

while True:
    total_pages = get_number("How many pages does the book have? ")
    if total_pages > 0:
        break
    print("The book must have at least 1 page.")

while True:
    pages_read = get_number("How many pages have you read? ")
    if pages_read <= total_pages:
        break
    print("Pages read cannot be more than", total_pages)

print("Enter dates as MM DD YYYY")
issue_date = get_date("Issue date: ")

while True:
    due_date = get_date("Due date: ")
    if due_date >= issue_date:
        break
    print("Due date cannot be before the issue date.")

percent = pages_read / total_pages * 100
days_left = (due_date - issue_date).days
pages_left = total_pages - pages_read

print("-----------------------------------------")
print("Message")
print("-----------------------------------------")
print("You have read", int(percent), "% of the book.")
print("You have", days_left, "day(s) left to return the book.")

if pages_left == 0:
    print("You have finished the book!")
elif days_left > 0:
    pages_per_day = pages_left // days_left
    if pages_left % days_left > 0:
        pages_per_day = pages_per_day + 1
    print("You have", pages_left, "page(s) left. Read", pages_per_day, "pages a day.")
else:
    print("You have", pages_left, "page(s) left and no days left.")
print("-----------------------------------------")