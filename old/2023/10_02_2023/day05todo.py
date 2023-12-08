todos = []
while True:
    user_action = input("Type add, show, edit or exit : ")
    user_action = user_action.strip()  # user action without strip will not execute if whitespace is present
    match user_action.strip():
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo)
        case 'show':
            for index, item in enumerate(todos):
                # item = f"{index + 1 }.{item}"
                print(item)
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of the todo to edit : "))
            new_todo = input("enter new todo : ")
            todos[number-1] = new_todo
        case 'complete':
            number = int(input("Number of the todo completed : "))
            todos.pop(number - 1)
        case default:
            print("unknown cmd")

# experiment 1 : don't go outside for-loop
# experiment 2 : len()
# experiment 3 : enumerte() for str to . for i,j in enumerate("hello") print(i,j)
# a= enumerate(["b","b"])
# print(a)
# enumerate onject at 0xisxskd error
# list(a)
# ["b","b"]
# Bonus : sort method, .sort(reverse=true)
