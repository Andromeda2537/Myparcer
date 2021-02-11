import time
import random
from creating_directory import name_for_directory, creating_directories, file_name_creation
from funk import get_url
from funk import catalog


def get_src_for_one_section(link):
    """Accepts links to product from the catalog
     as an argument and returns links to images"""
    html = get_url(link).text
    src = catalog(html, 'a', 'img', 'src', 'https://gastronomia.by', class_="thumb shine", )
    return src


def saver(all_products_from_the_catalog):
    """Creates directory name, filenames,
     and writes data to the appropriate directories"""
    total = 0
    for link in all_products_from_the_catalog:
        src_for_pictures = get_src_for_one_section(link)
        directory_name = name_for_directory(link)
        creating_directories(directory_name)
        for every_src in src_for_pictures:
            response = get_url(every_src)
            file_name = file_name_creation(every_src)
            time.sleep(random.random())
            with open(directory_name + '/' + file_name, 'wb') as file:
                file.write(response.content)
        total += 1
    return total

