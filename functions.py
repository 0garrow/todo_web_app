def get_todos(filepath="todos.txt"):
    """
    Read a text file and return the list of
    to do items.
    """
    with open(filepath) as file_local:
        todos_local = file_local.readlines()
        todos_local = [i.rstrip().capitalize() for i in todos_local]
    return todos_local


def write_todos(todos_arg, filepath="todos.txt"):
    """ Write the todo items list in a text file. """
    todos_arg = [i + "\n" for i in todos_arg]
    with open(filepath, "w") as file:
        file.writelines(todos_arg)


if __name__ == "__main__":
    print("Hello")
