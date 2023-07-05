while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()  # user action without strip will not execute if whitespace is present
    match user_action.strip():
        case 'add':
            todo = input("Enter a todo : ") + "\n"

            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            todos.append(todo)

            with open('todos.txt', 'w') as file:
                file.writelines(todos)


        case 'show':

            with open('todos.txt', 'r') as file:
                todos = file.readlines()

            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
                item = f"{index + 1}.{item}"
                print(item)
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of the todo to edit : "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            new_todo = input("enter new todo : ")
            todos[number - 1] = new_todo + "\n"
            with open('todos.txt', 'w') as file:
                file.writelines(todos)

        case 'complete':
            number = int(input("Number of the todo completed : "))
            with open('todos.txt', 'r') as file:
                todos = file.readlines()
            index = number-1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message =f"Todo {todo_to_remove} was removed from the list"
            print(message)

        case default:
            print("unknown cmd")


