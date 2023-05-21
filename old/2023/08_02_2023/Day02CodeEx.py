"""
Coding Exercise 1
Create a program that prompts the user to input their name once.
Then, the program prints out the name once with the first letter capitalized.
"""

name = input("What is your name ? ")
print(name.capitalize())

"""
Coding Exercise 2
Create a program that prompts the user to input their name once. 
Then, the program repeatedly prints out the name with the first letter capitalized.
"""
x = 0
while x < 3: # should be true but as i am uaing single file no use of true
    print(name.capitalize())
    x = x + 1

"""
Coding Exercise 3
Create a program that prompts the user to input their name repeatedly. 
Then, the program repeatedly prints out the name with the first letter capitalized. 
"""
y = 0
while y < 3: # should be true but as i am uaing single file no use of true
    name1 = input("What is your name ? ")
    print(name1.capitalize())
    y = y + 1