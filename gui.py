import functions
import PySimpleGUI as sg

lable = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo", key='todo')
button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[lable], [input_box], [button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todos("todos.txt")
            print(todos)
            new_todo = values["todo"] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
        case sg.WIN_CLOSED:
            break

window.close()