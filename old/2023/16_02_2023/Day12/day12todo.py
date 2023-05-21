def get_todos(filepath):
    with open(filepath, 'r') as file:
        todos_local = file.readlines()
    return todos_local


def write_todos(filepath, todos_arg):
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()  # user action without strip will not execute if whitespace is present

    if user_action.startswith('add') or user_action.startswith('new'):
        todo = user_action[4:]

        todos = get_todos('todos.txt')

        todos.append(todo + '\n')

        write_todos('todos.txt', todos)

    elif user_action.startswith('show'):

        todos = get_todos('todos.txt')

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item = f"{index + 1}.{item}"
            print(item)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])

            todos = get_todos('todos.txt')

            new_todo = input("enter new todo : ")
            todos[number - 1] = new_todo + "\n"

            write_todos('todos.txt', todos)

        except ValueError:
            print("Your cmd is invalid.")
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])

            todos = get_todos('todos.txt')

            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            write_todos('todos.txt', todos)

            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("No Number of that number")
            continue


    elif user_action.startswith(exit):
        break
    else:
        print("cmd is not valid")

# experiment 1 : scopes
