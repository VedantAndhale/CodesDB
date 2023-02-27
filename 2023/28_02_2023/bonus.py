import PySimpleGUI as gui
Label1 = gui.Text("Select Files to Compress: ")
input1 = gui.Input()
choose_button1 = gui.FileBrowse("Choose")
Label2 = gui.Text("Select destination folder: ")
input2 = gui.Input()
choose_button2 = gui.FolderBrowse("Choose")

compress = gui .Button("Compress")
windows = gui.Window("File Compressor",
                    layout=[[Label1,input1,choose_button1],
                            [Label2,input2,choose_button2]])
windows.read()
windows.close()