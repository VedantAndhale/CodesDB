"""
Coding Exercise 2
Write a program that reads the essay.txt file 
and returns the number of characters contained in the file.
"""

file = open('files/essay.txt', 'r')
eassy =file.read()
print(len(eassy))