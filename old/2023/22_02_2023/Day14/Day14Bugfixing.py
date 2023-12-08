"""
Bug fixing 1
The program depicted below consists of two Python files.
The program tries to count and print out the number of periods in the
"Trees are good. Grass is green." .
However, running the main.py file returns an error.
Please fix the error.
main.py:
    import functions
    nr_of_periods = count("Trees are good. Grass is green.")
    print(nr_of_periods)

functions.py:
    def count(phrase):
        return phrase.count('.')
make:
 nr_of_periods = functions.count("Trees are good. Grass is green.")

Bug fixing 2
The same program as in exercise 1 now is throwing yet another error.
Hunt the error down and fix it.
main.py:
    import functions.py
    nr_of_periods = functions.count("Trees are good. Grass is green.")
    print(nr_of_periods)
functions.py:
    def count(phrase):
        return phrase.count('.')

make:
import functions

Bug fixing 3

There is another error in the same program. Please fix the error.
main.py:
    from functions import count
    nr_of_periods = functions.count("Trees are good. Grass is green.")
    print(nr_of_periods)
functions.py:
    def count(phrase):
        return phrase.count('.')

make:
nr_of_periods = count("Trees are good. Grass is green.")

"""
