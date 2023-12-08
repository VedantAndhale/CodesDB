
import PySimpleGUI as gui
from converter import convert
Label1 = gui.Text("Enter feet: ")
input1 = gui.Input(key="feet")

Label2 = gui.Text("Enter inches: ")
input2 = gui.Input(key="inche")

convert_btn = gui .Button("Convert")
conversions = gui.Text("", key="conversion")
exit_btn = gui.Button("Exit")
windows = gui.Window("Convertor",
                    layout=[[Label1,input1],[Label2,input2],
                            [convert_btn,exit_btn,conversions]])

while True:
    event, values = windows.read()
    feet = float(values["feet"])
    inches = float(values["inche"])
    result = convert(feet, inches)
    windows["conversion"].update(value=f"{result} m", text_color="white")
    match event:
        case "Exit":
            break
        case gui.WIN_CLOSED:
            break

windows.close()