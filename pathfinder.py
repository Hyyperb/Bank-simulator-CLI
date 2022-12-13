import os.path

def path(relpath):

    my_path = os.path.abspath(os.path.dirname(__file__))
    path = os.path.join(my_path,relpath)

    return path