import functions
import PySimpleGUI as sg
import time

sg.theme("Black")
clock = sg.Text('',key="clock")
label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip="Enter todo",key="todo")
# add_button = sg.Button("Add")
add_button = sg.Button(size=10,image_source="add.png",mouseover_colors="LightBlue",
                       tooltip="Add Todo",key="Add")

list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True,size=[45,10])
edit_button = sg.Button("Edit")
# complete_button = sg.Button("Complete")
complete_button = sg.Button(size=10,image_source="complete.png",mouseover_colors="LightBlue",
                       tooltip="Add Todo",key="Complete")

exit_button = sg.Button("Exit")
windows = sg.Window('My Todo App',
                    layout=[[clock],[label],[input_box,add_button],
                            [[list_box,edit_button,complete_button],[exit_button]]],
                    font=('Helvetica',20))
while True:
    event,values = windows.read(timeout=10)
    windows["clock"].update(value=time.strftime("%b %d,%y %H:%M:%S"))

    match event:
        case "Add":
            todos =functions.get_todos()
            new_todo =values['todo']+ "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            windows['todos'].update(values=todos)

        case "Edit":
            try:
                todo_to_edit = values['todos'][0]
                new_todo = values['todo']

                todos = functions.get_todos()
                index = todos.index(todo_to_edit)
                todos[index] = new_todo
                functions.write_todos(todos)
                windows['todos'].update(values=todos)
            except IndexError:
                sg.popup("Please selct an item first.",font=("Helvetica",20))

        case 'todos':
            windows['todo'].update(value=values['todos'][0])
        case 'Complete':
            todo_to_complete = values['todos'][0]
            todos = functions.get_todos()
            todos.remove(todo_to_complete)
            functions.write_todos(todos)
            windows['todos'].update(values=todos)
            windows['todo'].update(value='')
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

windows.close()
