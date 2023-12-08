def get_todos():
    with open('todos.txt', 'r') as file_local:
        todos_local = file.readlines()
    return todos


while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()  # user action without strip will not execute if whitespace is present

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = get_todos()

        todos.append(todo + '\n')

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith('show'):

        todos = get_todos()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item = f"{index + 1}.{item}"
            print(item)
    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = get_todos()

            new_todo = input("enter new todo : ")
            todos[number - 1] = new_todo + "\n"
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
        except ValueError:
            print("Your cmd is invalid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)
            with open('todos.txt', 'w') as file:
                file.writelines(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("No Number of that number")
            continue


    elif user_action.startswith(exit):
        break
    else:
        print("cmd is not valid")

# experiment 1 :
# Bonus :
