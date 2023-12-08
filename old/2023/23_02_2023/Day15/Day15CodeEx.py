"""
Coding Exercise 1
Your task is to create a program that generates a random whole number.
Here is how the program should behave:
"""
import random

lower =int(input("Enter Lower bound: "))
upper =int(input("Enter upper bound: "))
random_numb = random.randint(lower, upper)
print(random_numb)