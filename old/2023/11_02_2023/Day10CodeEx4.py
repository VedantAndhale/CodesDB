"""
Coding Exercise 4
Create a program that generates multiple text files by iterating 
over the filenames list. 
The text Hello should be written inside each generated text file.
"""

files = ['ved.txt', 'ant.txt', 'vedant.txt']

for file in files:
    file = open(file, 'w')
    file.write("File Gengrated .....")
    file.close()