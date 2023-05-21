import PySimpleGUI as gui
from zip import make_archive

Label1 = gui.Text("Select Files to Compress: ")
input1 = gui.Input()
choose_button1 = gui.FileBrowse("Choose",key="files")
Label2 = gui.Text("Select destination folder: ")
input2 = gui.Input()
choose_button2 = gui.FolderBrowse("Choose",key="folder")

compress = gui .Button("Compress")
windows = gui.Window("File Compressor",
                    layout=[[Label1,input1,choose_button1],
                            [Label2,input2,choose_button2],
                            [compress]])

while True:
    event,values=windows.read()
    filepaths = values["files"].split(";")
    folder = values["folder"]
    make_archive(filepaths,folder)
windows.read()
windows.close()