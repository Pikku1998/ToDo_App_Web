FILEPATH = 'todos.txt'


def get_todos(filepath=FILEPATH):
    """ reads the text file and returns the todos in the file """
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
        return todos_local


def write_todos(todos_local, filepath=FILEPATH):
    """ writes the todos to the text file returns nothing """
    with open(filepath, 'w') as file_local:
        file_local.writelines(todos_local)