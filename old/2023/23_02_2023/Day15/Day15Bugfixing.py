"""
Bug fixing 1
Please have a look at the following scripts:

parsers.py

    def parse(user_input):
        //doc string
        Extract the values split by a comma in a string
        and return the two values via a dictionary.
        //doc string
        # Get the two values in a list
        parts = user_input.split(" ")
        
        # Store the two values in variables 
        lower_bound = float(parts[0])
        upper_bound = float(parts[1])
        
        # Inject the values in a dictionary
        return {"lower_bound": lower_bound, "upper_bound": upper_bound}
main.py

    from parsers import parse
    import random

    # Ask the user to enter a lower and an upper bound divided by a comma
    user_input = input("Enter a lower bound and an uppwer bound divided a comma (e.g., 2,10)")

    # Parse the user string by calling the parse function
    parsed = parse(user_input)

    # Pick a random int between the two numbers
    rand = random.randint(parsed['lower_bound'], parsed['upper_bound'])

    print(rand)

When the user executes main.py file, an error is produced.
 Place the two files in your IDE and try to debug the program.

 make:
parts = user_input.split(",")

"""
