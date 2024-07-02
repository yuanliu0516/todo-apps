import functions
import FreeSimpleGUI as sq
# 创建界面的第一个button"add"， 注意这里的todo
label = sq.Text("Type in a to-do")
input_box = sq.InputText(tooltip="Enter todo", key='todo')
add_button = sq.Button('Add')

# 创建界面的第二个button 'edit' 以及内容
# 我们需要把todo里面的values加到edit的界面里面 这样可以选择 通过call我们function里面的get_todo()可以直接
# 把里面的value加进去 注意这里的key是todos
list_box = sq.Listbox(values=functions.get_todo(), key='todos', enable_events=True, size=[45,10])
edit_button = sq.Button('Edit')
window = sq.Window('My TO-Do App',
                   layout=[[label],
                           [input_box, add_button],
                           [list_box, edit_button]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(1, event)
    print(2, values)
    print(3, values['todos'])
    match event:
        case "Add":
            todos = functions.get_todo()
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case sq.WINDOW_CLOSED:
            break

        case "Edit":
            todo_to_edit = values['todos'][0]
            print(todo_to_edit)
            new_todo = values["todo"]

            todos = functions.get_todo()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todo(todos)
            window['todos'].update(values=todos)
        case 'todos':
            window['todo'].update(value=values['todos'][0])




    # if event == sq.WINDOW_CLOSED:
    #     break
window.close()