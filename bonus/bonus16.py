import PySimpleGUI as sg
from zip_creator import make_archive

app_title = "Compressing tool"
label1 = sg.Text("Select files to compress:")
label2 = sg.Text("Select destination folder:")

input1 = sg.Input()
input2 = sg.Input()

choose_button1 = sg.FilesBrowse("Choose", key="files_to_compress")
choose_button2 = sg.FolderBrowse("Choose", key="folder")
compress_button = sg.Button("Compress")
output_label = sg.Text(key="output", text_color="green")

window = sg.Window(app_title, layout=[[label1, input1, choose_button1],
                                      [label2, input2, choose_button2],
                                      [compress_button, output_label]])
while True:
    event, values = window.read()
    print(event, values)
    filepaths = values["files_to_compress"].split(";")
    folder = values["folder"]
    print(filepaths)
    make_archive(filepaths, folder)
    window["output"].update(value="Compression completed")

window.close()
