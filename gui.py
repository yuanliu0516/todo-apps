import functions
import FreeSimpleGUI as sq

label = sq.Text("Type in a to-do")
input_box = sq.InputText(tooltip="Enter todo")
add_button = sq.Button('add')


window = sq.Window('My TO-Do App', layout=[[label],[input_box, add_button]])
window.read()
window.close()