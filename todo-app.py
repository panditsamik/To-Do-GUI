import PySimpleGUI as sg
import get_todos
import time
import os

if not os.path.exists("docs.txt"):
    with open("docs.txt", "w") as file:
        pass

sg.theme("Dark Black")

text_1 = sg.Text("Enter TO-DO :")
input_1 = sg.Input(key="input", tooltip="Enter your TO-DO")
btn_1 = sg.Button("Add", key="Add", tooltip="Add button")
time_text = sg.Text(".", key="now")

list_box = sg.Listbox(values=get_todos.getTodos(),
                      enable_events=True,
                      key="list_box",
                      size=(44, 12),
                      tooltip="To-DO Lists"
                      )
btn_2 = sg.Button("Edit",
                  key="Edit")

btn_3 = sg.Button("Exit")
btn_4 = sg.Button("Delete")

window = sg.Window("My To-Do App",
                   layout=[[time_text],
                           [text_1],
                           [input_1, btn_1],
                           [list_box, btn_2, btn_4],
                           [btn_3]],
                   font=("Oswald", 18)
                   )

while True:
    events, dict = window.read(timeout=10)
    window['now'].update(value=time.strftime("%b %d, %Y  %H:%M:%S"))
    match events:
        case "Add":
            data = get_todos.getTodos()
            data.append(dict['input'] + "\n")
            get_todos.writeTodos(data)
            window['list_box'].update(values=get_todos.getTodos())
        case "Edit":
            try:
                getdata = get_todos.getTodos()
                index = getdata.index(dict['list_box'][0])
                getdata[index] = dict['input']
                get_todos.writeTodos(getdata)
                window['list_box'].update(values=getdata)
            except IndexError:
                sg.popup("Please select an item first!", font=("Times New Roman", 10))
        case "Delete":
            try:
                getdata = get_todos.getTodos()
                index = getdata.index(dict['list_box'][0])
                fineData = getdata[index]
                getdata.remove(fineData)
                get_todos.writeTodos(getdata)
                window['list_box'].update(values=getdata)
            except IndexError:
                sg.popup("Please select an item first!", font=("Times New Roman", 10))
        case "list_box":
            selected = dict['list_box'][0]
            window['input'].update(value=selected)
        case sg.WIN_CLOSED:
            break
        case "Exit":
            break

window.close()
