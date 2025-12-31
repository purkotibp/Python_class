#  <!-- <!-- Assignment 5: Recursive Logic & Problem Solving
# Task 1: Recursive Palindrome (String Slicing)
# Goal: Understand how recursion can "shrink" a problem from both ends simultaneously without using loops.
# The Problem: Given a string (e.g., "RACECAR" or "LEVEL"), write a recursive function to check if it is a palindrome.
# Logic: Compare the first and last characters of the string. If they match, call the function again on the "inner" part of the string (the substring with the first and last letters removed).
# Constraint: Do not use loops or the string reversal trick [::-1].
# Base Case: If the string has 0 or 1 characters, return True. If the first and last characters don't match at any point, return False.   -->



def palindrome(string):
    if len(string)<=1:
        return True
    else:
        if string[0]== string[-1]:
            return palindrome(string[1:-1])
        else:
            return False

string = "racecar"
print(palindrome(string))

#find the next possible leap year using recursive function
def Leap_year(year):
    if year % 400 == 0:
        return True
    elif year % 100 == 0:
        return False
    elif year % 4 == 0:
        return True
    else:
        return False

year = 2021
print(Leap_year(year))

# Task 2: Sum of Digits (Mathematical Recursion)
# Goal: Practice mathematical extraction using modulo % and floor division // in a recursive context.
# The Problem: Take an integer input from the user (e.g., 1234) and return the sum of its digits ($1 + 2 + 3 + 4 = 10$).
# Logic: Extract the last digit using % 10 and add it to the result of the function called on the remaining digits (found using // 10).
# Constraint: Do not convert the number to a string. Use only mathematical operations.
# Base Case: If the number is less than 10, the sum is simply the number itself.
 
def sum_of_digits(n):
    if n < 10:
        return n
    return (n % 10) + sum_of_digits(n // 10)
num = int(input("Enter an integer: "))
print("Sum of digits:", sum_of_digits(num))





 