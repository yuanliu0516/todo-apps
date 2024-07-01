# from functions import get_todos, write_todos
import functions
import time
now=time.strftime("%b %d, %Y %H:%M:%S")
print('It is' , now)
while True:
    user_action = input('Type add, show, edit, complete or exit:')
    user_action = user_action.strip()

    if user_action.startswith('add'):
        todo = user_action[4:]
        # todos is not local variable, it's a global variable
        todos = functions.get_todo()
        todos.append(todo+'\n')
        functions.write_todo(todos)

    elif user_action.startswith('show'):
        todos = functions.get_todo()
        for index, item in enumerate(todos):
            item = item.strip('\n')
            row = f'{index + 1} - {item}'
            print(row)

    elif user_action.startswith('edit'):
        try:
            number = int(user_action[5:])
            print(number)
            number = number - 1
            todos = functions.get_todo()
            new_todo = input('Enter new todo: ')
            todos[number] = new_todo + '\n'
            functions.write_todo(todos)
        except ValueError:
            print('Your command is not valid.')
            continue

    elif user_action.startswith('complete'):
        try:
            number = int(user_action[9:])
            todos = functions.get_todo()
            index = number - 1
            todo_to_remove = todos[index].strip('\n')
            todos.pop(index)

            functions.write_todo(todos)
            message = f'Todo {todo_to_remove} was removed from the list.'
            print(message)
        except IndexError:
            print('There is no item with that number.')
            continue
    elif 'exit' in user_action:
        break
    else:
        print('Command is not valid')
print('Bye!')
