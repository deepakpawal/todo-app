import functions as f
import FreeSimpleGUI as sg

label=sg.Text("Type in a to-do")
input_box= sg.InputText(tooltip="Enter todo",key='todo')
exit_buttton=sg.Button("Exit")
add_button = sg.Button("Add")
edit_button=sg.Button("Edit")
list_box=sg.Listbox(values=f.get_todos(),key='todos',enable_events=True, size=[45, 10])

window = sg.Window('My To-Do App',
                   layout=[[label],[input_box,add_button],[list_box,edit_button],[exit_buttton]],
                   font=('Aptos', 21))
while True:
     event,values=window.read()
     print(event)
     print(values)
     match event:
        case "Add":
            todos = f.get_todos()
            todos.append(values["todo"] + "\n")
            f.write_todos(todos)
            window['todos'].update(values=todos)

        case "Edit":
            x=values["todos"][0]
            new_todo=values['todo']+ '\n'

            todos=f.get_todos()
            index=todos.index(x)
            todos[index]=new_todo
            f.write_todos(todos)
            window['todos'].update(values=todos)

        case "todos":
            window['todo'].update(value=values["todos"][0])

        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()