import functions
import PySimpleGUI as sg

lable = sg.Text("Type in a todo")
input_box = sg.InputText(tooltip="Enter todo")
button = sg.Button("Add")

window = sg.Window('My To-Do App', layout=[[lable, input_box, button]])
print("Hello")
window.read()
window.close()