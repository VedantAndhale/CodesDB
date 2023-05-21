"""
Bug fixing 1
The program below intends to find out how many items have at least one
underscore ("_") character in them.
However, there is an error with the code. Try to find and fix it.
    ids = ["XF345_89", "XER76849", "XA454_55"]
    x = 0
    for id in ids:
    if '_' in id:
        x = x + 1
    print(x)

indentation problem it should be like below
ids = ["XF345_89", "XER76849", "XA454_55"]
x = 0
for id in ids:
    if '_' in id:
        x = x + 1
print(x)


Bug fixing 2
This program also intends to find out how many items have an underscore
in them. However, the program has a bug. It doesn't return an error message,
but it returns:
    1
    1
    2
Instead, the expected output is:
2
Try to fix the program so it returns the expected output.
Here is the buggy program:
    ids = ["XF345_89", "XER76849", "XA454_55"]
    x = 0
    for id in ids:
        if '_' in id:
            x = x + 1
        print(x)

problem already fixed in above code

Bug fixing 3
Fix the program below so it prints out "OK" when the perimeter is less than
14 and the area is less than 8.
    length = float(input("Enter length: "))
    width = float(input("Enter width: "))
    perimeter = (length + width) * 2
    area = length * width
    print("Perimeter is", perimeter)
    print("Area is", area)
    if perimeter < 14 and area > 10:
        print("OK")
    else:
        print("NOT OK")

corrected it

length = float(input("Enter length: "))
width = float(input("Enter width: "))
perimeter = (length + width) * 2
area = length * width
print("Perimeter is", perimeter)
print("Area is", area)
if perimeter < 14 and area < 8 :
    print("OK")
else:
    print("NOT OK")

"""