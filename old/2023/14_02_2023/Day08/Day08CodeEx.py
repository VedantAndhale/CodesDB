"""
Coding Exercise 1
A client wants to buy a coin-flip probability program from you.
The programs should work like this:
1. The user runs the program.
The program asks the user to enter "head" or "tail".
The user flips a coin on their desk, table, floor, etc.,
and then enters "head" or "tail".
The user does the same over and over again.

Throw the coin and enter head or tail here: ? tail
heads: 0.0%
Throw the coin and enter head or tail here: ? head
heads: 50.0%

In each cycle, the program should return the current percentage
of heads in the program, similar to what you see in the screenshot above.
Also, you should write each user entry (i.e., head or tail) in a text file
using a with-context manager, one entry per line.
"""


while True:
    enter_action = input("wanna play use start or exit for end: ")
    match enter_action:
        case "start" :
            with open("coin_sides.txt", 'r') as file:
                coin_sides = file.readlines()

            coin_side = input("Throw the coin and enter head or tail here: ")
            coin_side = coin_side + "\n"

            coin_sides.append(coin_side)

            with open("coin_sides.txt", 'w') as file:
                file.writelines(coin_sides)

            numb_heads = coin_sides.count("head\n")
            percentage = numb_heads / len(coin_sides) * 100

            print(f"Heads: {percentage}%")
        case "exit" :
            break