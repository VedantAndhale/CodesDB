import PySimpleGUI as gui
from extractor import extraactor_archive

Label1 = gui.Text("Select Files to Extractor: ")
input1 = gui.Input()
choose_button1 = gui.FileBrowse("Choose",key="archive")

Label2 = gui.Text("Select destination folder: ")
input2 = gui.Input()
choose_button2 = gui.FolderBrowse("Choose",key="folder")

extractor = gui.Button("Extract")
opt_label = gui.Text(key="output",text_color="green")

windows = gui.Window("File Extractor",
                    layout=[[Label1,input1,choose_button1],
                            [Label2,input2,choose_button2],
                            [extractor,opt_label]])

while True:
    event,values=windows.read()
    archivepath = values["archive"]
    dest_dir = values["folder"]
    extraactor_archive(archivepath,dest_dir)
    windows["output"].update(value="Extraction complete")
windows.close()