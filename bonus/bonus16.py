import PySimpleGUI as sg

app_title = "Compressing tool"
label1 = sg.Text("Select files to compress:")
label2 = sg.Text("Select destination folder:")

input1 = sg.Input()
input2 = sg.Input()

choose_button1 = sg.FilesBrowse("Choose")
choose_button2 = sg.FolderBrowse("Choose")
compress_button = sg.Button("Compress")

window = sg.Window(app_title, layout=[[label1, input1, choose_button1],
                                      [label2, input2, choose_button2],
                                      [compress_button]])

window.read()
window.close()
