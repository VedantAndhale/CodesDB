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

            # new_todo=[]
            # for item in todos:
            #     new_item=item.strip("\n")
            #     new_todo.append(new_item)
            # new way
            new_todos = [item.strip('\n') for item in todos]

            for index, item in enumerate(new_todos):
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

# Bonus :
# replace using list comprehension
# filenames=[filename.replace('.','-')]
# 1.rep->1-rep above conversion
# filenames=[filename.replace('.','-')+ .txt for filename in filenames]
# concatination 1-rep.txt