import pathlib
import zipfile

def extraactor_archive(archivepath,dest_dir):
    with zipfile.ZipFile(archivepath,'r') as archive:
        archive.extractall(dest_dir)


if __name__=="__main__":
    extraactor_archive("compressed.zip","/home/vedant/PycharmProjects/pythonProject/app1/Day18/bonus")