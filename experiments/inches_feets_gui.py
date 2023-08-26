import PySimpleGUI as sg
from bonus import converters14 as converting

app_tile = "Convertor"
label_feet = "Enter feet:"
label_inch = "Enter inches:"

label1 = sg.Text(label_feet)
label2 = sg.Text(label_inch)
label3 = sg.Text(key="meter")

input_feet = sg.InputText(key="feet")
input_inches = sg.InputText(key="inches")
convert_button = sg.Button("Convert", key="convert")

layout = [[label1, input_feet], [label2, input_inches], [convert_button, label3]]

window = sg.Window(app_tile, layout=layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "convert":
            try:
                meter = converting.convert(int(values['feet']), int(values['inches']))
                label3.update(str(meter) + " meters")
            except ValueError:
                label3.update("Incorrect values!")
        case sg.WIN_CLOSED:
            break
print("Bye")
window.close()
