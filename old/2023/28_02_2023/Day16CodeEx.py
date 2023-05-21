import PySimpleGUI as gui
Label1 = gui.Text("Enter feet: ")
input1 = gui.Input()

Label2 = gui.Text("Enter inches: ")
input2 = gui.Input()

convert = gui .Button("Convert")
windows = gui.Window("Convertor",
                    layout=[[Label1,input1],[Label2,input2],[convert]])
windows.read()
windows.close()