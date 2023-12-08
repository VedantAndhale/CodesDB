"""
Coding Exercise 1
Create a program that does the following:
1. Prompts the user to input the country they are from.
2. If the user enters the word USA, the program prints out Hello.
3. If the user enters the word  India, the program prints out Namaste.
4. If the user enters the word Germany, the program prints out Hallo.
Note: Strings are case-sensitive in Python,
meaning germany and Germany are treated as two different strings.
"""
country = input("Enter your country(USA,India,Germany) : ")
country = country.strip()
match country:
    case "USA":
        print("hello")
    case "India":
        print("Namaste")
    case "Germany":
        print("Hallo")
    case _:
        print("Strings are case-sensitive")

"""
Coding Exercise 2
    ingredients = ["john smith", "sen plakay", "dora ngacely"]
Copy-paste the above line into your IDE and write a for-loop below 
that line that makes the program produce the following output:
1st word letter capital of words
Tip:  Use the str.title() method to convert strings to Title Case.
"""
ingredients = ["john smith", "sen plakay", "dora ngacely"]
for ingredient in ingredients:
    ingredient = ingredient.title()
    print(ingredient)