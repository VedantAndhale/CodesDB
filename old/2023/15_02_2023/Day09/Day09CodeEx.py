"""
Coding Exercise 1
Write a program that asks users to enter a password.
Then, it checks if the password length is greater than 7 and returns
"Great password there!".
"""


"""
Coding Exercise 2
Extend the program we built in Coding Exercise 1 by adding a new feature. 
The new feature should allow the program to return
 "Password is OK, but not too strong" when 
 the password is exactly seven characters long.
"""
password = input("Enter new password: ")

if len(password) > 7:
    print("Your Password is Strong")
elif len(password) == 7:
    print("Password is OK, but not too strong")
else:
    print("Your Password is Weak")


