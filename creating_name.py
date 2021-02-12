def get_name_directory(link):
    """Returns the last element for the directory name
    from the full link passed as an argument"""
    directory_name = link.split('/')[-2]
    return directory_name


def get_file_name(src):
    """Creates a filename using the last element from a string"""
    file_name = src.split('/')[-1]
    return file_name
