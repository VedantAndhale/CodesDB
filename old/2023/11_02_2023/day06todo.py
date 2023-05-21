todos = []
while True:
    user_action = input("Type add, show, edit or exit : ")
    user_action = user_action.strip()  # user action without strip will not execute if whitespace is present
    match user_action.strip():
        case 'add':
            todo = input("Enter a todo : ") + "\n"
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            todos.append(todo)
            file = open('todos.txt', 'w')
            file.writelines(todos)
            file.close()
        case 'show':
            file = open('todos.txt', 'r')
            todos = file.readlines()
            file.close()
            for index, item in enumerate(todos):
                item = f"{index + 1}.{item}"
                print(item)
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of the todo to edit : "))
            new_todo = input("enter new todo : ")
            todos[number - 1] = new_todo

        case 'complete':
            number = int(input("Number of the todo completed : "))
            todos.pop(number - 1)
        case default:
            print("unknown cmd")

# experiment 1 : always check the path of file always absolute vs relative.
# experiment 2 : \n \t
# Bonus : if you have two different list ex. one with flies and other with content
# we cant use enumarate we use zip() for this purpose. enumerate is used for index content
# zip is used for contente content 1-1 mapping.
