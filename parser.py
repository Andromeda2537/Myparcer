import time
import random
from creating_name import get_name_directory, get_file_name
from creating_directory import directory_creation
from get_links_on_product import get_url, get_src


def saver(all_links_from_the_catalog, address):
    """Creates directory name, filenames,
     and writes data to the appropriate directories"""
    total = 0
    for link in all_links_from_the_catalog:
        src_for_pictures = get_src(link)
        directory_name = get_name_directory(link)
        directory_creation(directory_name)
        for every_src in src_for_pictures:
            if every_src.split('/')[-2] == 'gastronomia.bydata:image':
                continue
            full_links_for_src = address + every_src
            response = get_url(full_links_for_src)
            file_name = get_file_name(every_src)
            time.sleep(random.random())
            with open(directory_name + '/' + file_name, 'wb') as file:
                file.write(response.content)
        total += 1
    return total
