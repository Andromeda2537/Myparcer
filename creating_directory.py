import os


def name_for_directory(link):
    """Returns the last element for the directory name
    from the full link passed as an argument"""
    directory_name = link.split('/')[-2]
    return directory_name


def creating_directories(directory_name):
    """Accepts as an argument the result of the 'name_for_directory' function.
     If there is no directory with the name received from the function,
     it creates a directory"""
    if not os.path.isdir(directory_name):
        os.makedirs(directory_name)
    return directory_name


def file_name_creation(src):
    file_name = src.split('/')[-1]
    return file_name
