"""
Bug fixing 1
Have a look at the program below:

    waiting_list = ["john", "marry"]
    name = input("Enter name: ")

    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")

When the user enters the name of one of the waiting_list members,
 the program returns the index of that name.
 For example, when the user enters "john", 0 is printed out.

Enter name: john
john's turn is 0

If the user enters a name that is not in the list,
such as "zen", the program throws an error.

Change the program, so it prints out "zen is not in the list"
instead of returning an error when the user enters "zen" or
any other name that is not in the list.
"""
waiting_list = ["john", "marry"]
name = input("Enter name: ")
try:
    number = waiting_list.index(name)
    print(f"{name}'s turn is {number}")
except ValueError:
    exit(f"{name} is Not in the list")