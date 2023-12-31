import functions
import PySimpleGUI as sg

label = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter a todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key="todos",
                      enable_events=True, size=[45, 10])
edit_button = sg.Button("Edit")
close_button = sg.Button("Close")
app_title = "My ToDo app"

layout = [[label], [input_box, add_button], [list_box, edit_button], [close_button]]
window = sg.Window(app_title,
                   layout=layout,
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print("Hello")
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case "Edit":
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + "\n"

            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
            print(todo_to_edit)
        case 'todos':
            window['todo'].update(value=values['todos'][0])
        case 'Close':
            window.close()
        case sg.WIN_CLOSED:
            break
print("Bye")
window.close()
