"""
Coding Exercise 3
Please download the members.txt file from the resources of this article.
Then, create a program that, whenever executed, 
asks the user to enter a new member in the command line: 
Add anew member: Solomon Right
Then, the member is added to members.txt. 
In this case, the text file content would be:
John Smith
Sen Lakmi
Sono Octonot
Solomon Right
"""

member = input("Enter a member : ")
file = open('files/members.txt', 'r')
members = file.readlines()
file.close()
members.append(member.title())
file = open('files/members.txt', 'w')
file.writelines(members)
file.close()

