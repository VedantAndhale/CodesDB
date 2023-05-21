todos = []
while True:
    user_action = input("Type add, show, edit or exit : ")
    user_action = user_action.strip()  # user action without strip will not execute if whitespace is present
    match user_action.strip():
        case 'add':
            todo = input("Enter a todo : ")
            todos.append(todo)
        case 'show':
            for item in todos:
                item = item.title()
                print(item)
        case 'exit':
            break
        case 'edit':
            number = int(input("Number of the todo to edit : "))
            number = number - 1
            new_todo = input("enter new todo : ")
            todos[number] = new_todo
        case default:
            print("unknown cmd")

# experiment 1 : Importance of types - str +int not possible but string * int possible '5'*10=5555555555
# experiment 2 : float vs int,convert types
# experiment 3 : list indexing - to find index use list_name.index(What you wanna find)
# Bonus to replace string aka item in list use str.replace(replace this, by this, occurence of word to be replaced if 1 mean only replace first) is temp to make permanent store in new variable
# tuple = ("1","2")