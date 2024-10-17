import functions as f
import FreeSimpleGUI as sg

label=sg.Text("Type in a to-do")
input_box= sg.InputText(tooltip="Enter todo",key='todo')
exit_buttton=sg.Button("Exit")
add_button = sg.Button("Add")

window = sg.Window('My To-Do App',
                   layout=[[label],[input_box,add_button],[exit_buttton]],
                   font=('Aptos', 21))
while True:
     event,values=window.read()
     match event:
        case "Add":
            todos = f.get_todos()
            todos.append(values["todo"] + "\n")
            f.write_todos(todos)

        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()