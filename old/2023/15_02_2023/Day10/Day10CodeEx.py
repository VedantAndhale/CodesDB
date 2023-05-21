"""
Coding Exercise 1
Build a percentage calculator that gets from the user the "total value"
and the "value" and returns the percentage as shown below:
Enter total value: 50
Enter value: 20
That is 40.0%
The program should also print a message if the user doesn't
enter a number for the "total value or for the "value":
Enter total value: 50
Enter value: h1
You need to enter anumber, Run the program again.


Coding Exercise 2
As you might know, it is not mathematically possible to divide a number
by zero. Consequently, this is also not possible in Python either
-you will get a ZeroDivisionError if you try:

    >>> 20 / 0
    Traceback (most recent call last):
      File "<stdin>", line 1, in <module>
    ZeroDivisionError: division by zero

With that in mind, your task for this exercise is to extend the program
you created in Exercise 1 by displaying a message to the user when they
 enter 0 for the "total value".
"""


try:
    total_value =  int(input("Enter total value: "))
    value = float(input("Enter value: "))
    percentage = (value/total_value)*100
    print(f"That is {percentage}%")
except ValueError:
    exit("You need to enter a number, Run the program again.")
except ZeroDivisionError:
    exit("Your total value cannot be zero.")

