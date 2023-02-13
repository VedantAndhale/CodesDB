"""
Coding Exercise 5
Please download the three text files a.txt, b.txt, and c.txt 
from the resources. Then, create a program that reads each 
text file and prints out the content of each in the command line. 
The expected output would be like the following:
I am a.
I am b.
I am c.
"""

files = ['a.txt', 'b.txt', 'c.txt']
filename = f"files/{files}"
for file in filename:
    fileread = open(filename, 'r')
    reads = fileread.read()
    print(reads)
file.close()