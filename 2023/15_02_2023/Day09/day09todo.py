todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()  # user action without strip will not execute if whitespace is present

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item = f"{index + 1}.{item}"
            print(item)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("enter new todo : ")
        todos[number - 1] = new_todo + "\n"
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
    elif 'exit' in user_action:
        break
    else:
        print("cmd is not valid")

# experiment 1 : comparision operators
todos = []
while True:
    user_action = input("Type add, show, edit, complete or exit : ")
    user_action = user_action.strip()  # user action without strip will not execute if whitespace is present

    if 'add' in user_action or 'new' in user_action:
        todo = user_action[4:]

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        todos.append(todo)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'show' in user_action:

        with open('todos.txt', 'r') as file:
            todos = file.readlines()

        new_todos = [item.strip('\n') for item in todos]

        for index, item in enumerate(new_todos):
            item = f"{index + 1}.{item}"
            print(item)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        new_todo = input("enter new todo : ")
        todos[number - 1] = new_todo + "\n"
        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
        number = int(user_action[9:])
        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip('\n')
        todos.pop(index)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
    elif 'exit' in user_action:
        break
    else:
        print("cmd is not valid")

# experiment 1 : comparision operators


