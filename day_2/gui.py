import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo")
add_button = sg.Button("Add")
app_title = "My ToDo app"

window = sg.Window(app_title, layout=[[label], [input_box, add_button]])
window.read()
print("Hello")
window.close()
