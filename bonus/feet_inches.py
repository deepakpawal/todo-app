import FreeSimpleGUI as sg
from FreeSimpleGUI import popup


text_1 = sg.Text("Enter feet")
feet_input = sg.InputText(key="feet")
text_2=sg.Text("Enter inches")
inches_input=sg.InputText(key="inch")

output=sg.Text(key="output")

convert_button=sg.Button("Convert",key="calculate")
window = sg.Window("Convertor", layout=[[text_1,feet_input],[text_2,inches_input],[convert_button,output]])

while True:
    event,values = window.read()
    meter= float(values["feet"])* 0.3048 + float(values["inch"])*0.0254

    if event == 'calculate':
        window["output"].update(value=meter)


window.close()