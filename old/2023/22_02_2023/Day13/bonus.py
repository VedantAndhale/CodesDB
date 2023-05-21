feet_inches = input("Enter feet and inches: ")


def convert(feet_inches):
    parts = feet_inches.split(" ")
    feet = float(parts[0])
    inches = float(parts[1])
    meters = feet * 0.3048 + inches * 0.0254
    print(f"{feet} feet and {inches} inches is equal to {meters} meters.")
    # decoupling function
    # return feet,inches  method 1
    # return{"feet":feet,"Inches":inches} method 2 used parse/parsed key word


result=convert(feet_inches)
if result<1:
    print("Kid is too small.")
else:
    print("Kid can use the slide")