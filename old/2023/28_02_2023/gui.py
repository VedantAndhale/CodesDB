import functions
import PySimpleGUI as sg

label = sg.Text("Type in a Todo")
input_box = sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add")
windows = sg.Window('My Todo App', layout=[[label,input_box,add_button]])
windows.read()
windows.close()
