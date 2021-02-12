import os


def directory_creation(directory_name):
    """Creates a directory with the name given as an argument, if not present"""
    if not os.path.isdir(directory_name):
        os.makedirs(directory_name)
    return directory_name
