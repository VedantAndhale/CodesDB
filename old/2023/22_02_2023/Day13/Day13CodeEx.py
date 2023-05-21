"""
Coding Exercise 1
Define a function that has two parameters, year_of_birth and current_year .
The current_year parameter should be a default parameter with the current year
 as a default value.
The function should calculate and return the age of the user given
the year of birth and the current year.
Note: It is enough to define the function for this exercise
-no need to call it.


Coding Exercise 2
Your task for this exercise is to use the function you created in exercise 1.
Then, below the function definition, get the year of birth from the user
using an input function and then call and print the defined function to get
the user's age as output. Here is how the program should behave:
what is your year of birth? 1902
121

Coding Exercise 3
Extend the program you wrote in exercise 2 by printing a message
to the user instead of their age if their age is greater than 120.
Feel free to print any message that you like.

Coding Exercise 4
Write a program that gets a list of names from the user and
returns the number of names given. You are encouraged to use a function.
Here is how the program would work:
Enter names separated by commas(no spaces): john,jay,marry
3

"""

year_of_birth = int(input("what is your year of birth? "))


def birth(year_of_birth, current_year=2023):
    age = current_year - year_of_birth
    print(f"Your age is {age}")
    return age

result = birth(year_of_birth)
if result > 120:
    print("do take care of you health young man")
else:
    print(result)

names = input("Enter names separated by commas(no spaces): ")
def split_names(names):
    name=names.split(",")
    return len(name)

print(split_names(names))