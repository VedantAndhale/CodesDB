"""
Bug fixing 1
The code below tries to write the items of temperatures each in one line
in the file.txt list.
However, the code has an error. Try to fix the error.
    temperatures = [10, 12, 14]
    file = open("file.txt", 'w')
    file.writelines(temperatures)
use temp=[str(temps)+'\n' for temps in temprature on one temperature on single line.


Bug fixing 2
The code below tries to convert all the numbers to integers.
 However, the code has an error. Try to fix the error.
    numbers = [10.1, 12.3, 14.7]
    numbers = [int(number) for item in numbers]
    print(numbers)
it should be int(item) or for number in numbers


"""
