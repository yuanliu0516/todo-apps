def get_todo(filepath='todos.txt'):
    """ Read a text file and return the list of to_do items."""
    with open(filepath, 'r') as file_local:
        # create a local variable
        todos_local = file_local.readlines()
    return todos_local

# print(help(get_todo)) to check the get_todo() function


def write_todo(todos_arg, filepath='todos.txt'):
    """Write the to-do items in the next file """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_arg)
