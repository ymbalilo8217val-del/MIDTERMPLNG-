import random
import datetime

print("--- Program 1 ---")
print("Hello World")

print("--- Program 2 ---")
name = input("What is your name? ")
print("Hello", name)

print("--- Program 3 ---")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print("The sum is", a + b)

print("--- Program 4 ---")
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Average:", (a + b) / 2)

print("--- Program 5 ---")
midterm = float(input("Enter your midterm grade: "))
final = float(input("Enter your final grade: "))
print("Average:", midterm * 0.3 + final * 0.7)

print("--- Program 6 ---")
exam1 = float(input("First exam: "))
exam2 = float(input("Second exam: "))
exam3 = float(input("Third exam: "))
print("Average:", (exam1 + exam2 + exam3) / 3)

print("--- Program 7 ---")
average = int(input("Enter average: "))
if average >= 50:
    print("Passed")
else:
    print("Failed")

print("--- Program 8 ---")
num = int(input("Enter a number: "))
if num % 2 == 0:
    print(num, "is Even")
else:
    print(num, "is Odd")

print("--- Program 9 ---")
num = float(input("Enter a number: "))
if num > 0:
    print("Positive number")
elif num == 0:
    print("Zero")
else:
    print("Negative number")

print("--- Program 10 ---")
height = float(input("Enter height (m): "))
weight = float(input("Enter weight (kg): "))
bmi = weight / (height * height)
if bmi <= 18:
    print("Underweight, BMI:", bmi)
elif bmi <= 25:
    print("Normal weight, BMI:", bmi)
elif bmi <= 30:
    print("Overweight, BMI:", bmi)
else:
    print("Severely obese, BMI:", bmi)

print("--- Program 11 ---")
age = int(input("Enter age: "))
if age < 18:
    print("You are not old enough to get a driver's license")
else:
    print("You are old enough to get a driver's license")

print("--- Program 12 ---")
for i in range(1, 101):
    print(i)

print("--- Program 13 ---")
for i in range(1, 101):
    if i % 2 == 0:
        print(i)

print("--- Program 14 ---")
for i in range(1, 101):
    if i % 2 != 0:
        print(i)

print("--- Program 15 ---")
for i in range(1, 101):
    if i % 3 == 0 or i % 5 == 0:
        print(i)

print("--- Program 16 ---")
num = int(input("Enter a number: "))
for i in range(1, num + 1):
    print(i)

print("--- Program 17 ---")
short = int(input("Enter short side: "))
tall = int(input("Enter tall side: "))
print("Area:", short * tall)
print("Perimeter:", 2 * (short + tall))

print("--- Program 18 ---")
word = "hello"
for letter in word:
    print(letter)

print("--- Program 19 ---")
first = int(input("First number: "))
second = int(input("Second number: "))
total = 0
for i in range(first + 1, second):
    total = total + i
print("Sum of numbers between", first, "and", second, ":", total)

print("--- Program 20 ---")
choice = input("Press 1 for Cinema, 2 for Theater: ")
student = input("Are you a student? (Y/N): ")
price = 0
if choice == "1":
    price = 10
elif choice == "2":
    price = 5
if student == "Y" or student == "y":
    price = price / 2
print("You have to pay:", price)

print("--- Program 21 ---")
num = int(input("Enter a number: "))
is_prime = True
if num < 2:
    is_prime = False
for i in range(2, num):
    if num % i == 0:
        is_prime = False
if is_prime:
    print(num, "is a prime number")
else:
    print(num, "is not a prime number")

print("--- Program 22 ---")
numbers = []
even_sum = 0
odd_sum = 0
count = int(input("How many numbers? "))
for i in range(count):
    value = int(input("Enter a number: "))
    numbers.append(value)
for n in numbers:
    if n % 2 == 0:
        even_sum = even_sum + n
    else:
        odd_sum = odd_sum + n
print("Sum of even numbers:", even_sum)
print("Sum of odd numbers:", odd_sum)

print("--- Program 23 ---")
salary = float(input("Enter current salary: "))
rate = float(input("Enter raise rate (%): "))
new_salary = salary + salary * rate / 100
print("New salary:", new_salary)

print("--- Program 24 ---")
pi = 3.14159
radius = float(input("Enter the radius of a circle: "))
print("Diameter:", 2 * radius)
print("Circumference:", 2 * pi * radius)
print("Area:", pi * radius * radius)

print("--- Program 25 ---")
width = float(input("Enter width: "))
height = float(input("Enter height: "))
print("Area:", width * height)
print("Perimeter:", 2 * (width + height))

print("--- Program 26 ---")
lower = int(input("Enter lower number: "))
upper = int(input("Enter upper number: "))
secret = random.randint(lower, upper)
chances = 5
print("You have", chances, "chances to guess the number")
tries = 0
found = False
while tries < chances and found == False:
    tries = tries + 1
    guess = int(input("Guess a number: "))
    if guess == secret:
        print("You got it in", tries, "tries")
        found = True
    elif guess < secret:
        print("Too small")
    else:
        print("Too high")
if found == False:
    print("The number was", secret)
    print("Better luck next time")

print("--- Program 27 ---")
date = input("Enter the date (for example 09 02 2019): ")
days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
day_number = datetime.datetime.strptime(date, "%d %m %Y").weekday()
print(days[day_number])

print("--- Program 28 ---")
numbers = [1, 2, 4, 6, 7, 9, 10]
print("List:", numbers)
missing = []
for i in range(numbers[0], numbers[-1] + 1):
    if i not in numbers:
        missing.append(i)
print("Missing numbers:", missing)

print("--- Program 29 ---")
letters = ["a", "b", "c"]
text = "abcd"
all_found = True
for char in text:
    if char not in letters:
        all_found = False
print("All characters are in the list:", all_found)

print("--- Program 30 ---")
total = 0
even_sum = 0
even_count = 0
odd_sum = 0
odd_count = 0
while True:
    value = input("Enter an integer or type done: ")
    if value == "done":
        break
    value = int(value)
    total = total + value
    if value % 2 == 0:
        even_sum = even_sum + value
        even_count = even_count + 1
    else:
        odd_sum = odd_sum + value
        odd_count = odd_count + 1
print("Total sum:", total)
if even_count > 0:
    print("Even average:", even_sum / even_count)
else:
    print("Even average: 0")
if odd_count > 0:
    print("Odd average:", odd_sum / odd_count)
else:
    print("Odd average: 0")