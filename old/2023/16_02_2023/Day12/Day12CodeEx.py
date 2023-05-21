"""
Coding Exercise 1
Create a function that converts liters to cubic meters
knowing that 1000 liters make 1 cubic meter.
"""

milk_liters = int(input("Enter Milk in liters: "))


def convert(milk_liters):
    milk_cc = milk_liters / 1000
    print(f"{milk_liters} liters milk is {milk_cc} cubic meters.")
    return milk_cc


convert(milk_liters)


"""
Coding Exercise 2
Create a script that asks the user to enter a password. 
Then create a function that checks the strength of the user password. 
The function should return Strong Password if all of the following conditions
 are true:
Eight or more characters
At least one uppercase letter.
At least one digit.
Here is what happens when the user provides a password that satisfies all
three conditions:

similar output to day 9 bonus exercise. 
"""

password = input("Enter new password: ")

def check(password):
    result ={}
    if len(password) >= 8:
        result["length"] = True
    else:
        result["length"] = False

    digit = False
    for i in password:
        if i.isdigit():
            digit=True

    result["digit"] = digit

    uppercase = False
    for i in password:
        if i.isupper():
            uppercase=True

    result["uppercase"] = uppercase

    if all(result.values()):
        print("Strong Password")
    else:
        print("Weak Password")
    return 1

check(password)