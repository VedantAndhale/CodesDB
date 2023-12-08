
todos = []
while True:
    user_action = input("Type add, show, or exit : ")
    user_action = user_action.strip() #user action without strip will not execute if whitespace is present
    match user_action.strip():
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo)
        case 'show' :
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case default:
            print("unkown cmd")

# experiment 1 : Match-case use anything like default or _
# experiment 2 : Bitwise (or / |) Operator
# experiment 3 : for-loop
# Bonus str and list are considered as sequences
"""
for meal in 'meals':
    print(meal.capitalize())
output:
M
E
A
L
S
"""

