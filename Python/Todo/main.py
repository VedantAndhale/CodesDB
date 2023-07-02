todos = []
while True:
    user_action = input ("Type add or show: ")
    user_action = user_action.strip()
    match user_action :
         case 'add':
            todo = input("Enter a Todo: ")
            todos.append(todo)
         case 'show':
            for item in todo:
                print(item)
         case 'exit':
            break
         case _ :
            print("Hey, You Entered an unknown cmd !")
print('Bye!')






