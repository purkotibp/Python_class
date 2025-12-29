# Task 1: The "FizzBuzz" Classic (Pattern Logic)
# Goal: Practice multiples and modulo operations using loops and nested conditionals.
# The Problem:Write a program that prints numbers from 1 to 50.
# If the number is a multiple of 3, print "Fizz" instead of the number.
# If it is a multiple of 5, print "Buzz".
# If it is a multiple of both 3 and 5, print "FizzBuzz".
# Otherwise, just print the number.
for number in range(1, 51):
    if number % 3 == 0 and number % 5 == 0:
        print("FizzBuzz")
    elif number % 3 == 0:
        print("Fizz")
    elif number % 5 == 0:
        print("Buzz")
    else:
        print(number)


# Task 2: Find the Maximum and Minimum (Array Traversal)
# Goal: Understand how to keep track of state variables while looping through a list.
# The Problem:Given a list of numbers (e.g., [23, 45, 12, 56, 89, 3, 44]), write a loop to find the largest and smallest numbers in the list without using built-in functions like max() or min().
 
# Remarks: Please dont use the same method that we use in class.
numbers = [23, 45, 12, 56, 89, 3, 44]

largest = float('-inf')
smallest = float('inf')

for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

print("Largest number:", largest)
print("Smallest number:", smallest)


# ask 3: Reverse a Number (Mathematical Loop)
# Goal: Practice while loops and using the modulo % and floor division // operators.
# The Problem:Take an integer input from the user (e.g., 1234) and print it in reverse order (e.g., 4321).
# Constraint: Do not convert the number to a string. Use mathematical operations inside a while loop to extract digits one by one.
number = int(input("Enter a number: "))

reversed_number = 0

while number > 0:
    digit = number % 10# the last digit
    reversed_number = reversed_number * 10 + digit
    number = number // 10#Remove last digit

print("Reversed number:", reversed_number)

# Task 5: The Fibonacci Sequence (Algorithmic Thinking)
# Goal: Learn how to update multiple variables simultaneously within a loop.
# The Problem:Write a program to generate the first N terms of the Fibonacci sequence.
# The sequence starts: 0, 1, 1, 2, 3, 5, 8, 13, ... (Each number is the sum of the two preceding ones).
# Use a loop to calculate the next term and update your "previous" and "current" variables accordingly.

N = int(input("Enter number of terms: "))

a = 0
b = 1

for _ in range(N):
    print(a, end=" ")
    a, b = b, a + b

 

# Task 4: Prime Number Checker (Efficiency Logic)
# Goal: Understand the "break" statement and boolean flags.
# The Problem:Ask the user for a number and determine if it is a Prime Number.
# A prime number is only divisible by 1 and itself.
# Logic: Use a for loop to check if any number from 2 up to the square root of the input divides it perfectly. 
# Use an if/else block to print the final result.

num = int(input("Enter a number: "))

is_prime = True

if num <= 1:
    is_prime = False
else:
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False
            break

if is_prime:
    print("Prime number")
else:
    print("Not a prime number")
