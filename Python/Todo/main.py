todos = []
while True:
    user_action = input ("Type add,show or exit: ")
    user_action = user_action.strip()
    match user_action :
         case 'add':
            todo = input("Enter a Todo: ")
            todos.append(todo)
         case 'show':
            for index,item in enumerate(todo):
                print(f"{index+1}.{item}")
         case 'edit':
            number = int(input("Number of the todo to edit"))
            number = number-1
            new_todo = input("Enter new todo : ")
            todo[number] = new_todo
         case 'complete':
            number = int(input("Number of the todo to edit"))
            todos.pop(number-1)
         case 'exit':
            break
         case _ :
            print("Hey, You Entered an unknown cmd !")
print('Bye!')






