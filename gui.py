import functions
import FreeSimpleGUI as sq

label = sq.Text("Type in a to-do")
input_box = sq.InputText(tooltip="Enter todo", key='todo')
add_button = sq.Button('Add')


window = sq.Window('My TO-Do App',
                   layout=[[label], [input_box, add_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todo(todos)
        case sq.WINDOW_CLOSED:
            break

    # if event == sq.WINDOW_CLOSED:
    #     break
window.close()