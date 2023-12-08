"""
Coding Exercise 1
The code below is incomplete.
It should calculate and print out the maximum value of the grades list.
Please complete the function and then call it.

    def get_max():
        grades = [9.6, 9.2, 9.7]

The output of your code should be:
9.7

Hint: You can use the max(list) function to find the maximal value of a list.




def get_max():
    grades = [9.6, 9.2, 9.7]
    return print(max(grades))

get_max()
"""

"""

Coding Exercise 2
The function we wrote in exercise 1 returned 9.7.  
Change the function so this time it returns Max: 9.7, Min: 9.2 
where 9.7 is the maximum and 9.2 is the minimum. 
"""

def get_max():
    grades = [9.6, 9.2, 9.7]
    maximum = max(grades)
    minimum = min(grades)
    return print(f"Max: {maximum}, Min: {minimum}")


get_max()


