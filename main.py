from get_links_on_product import get_url
from get_links_on_product import get_tag_content, get_attribute_value, get_full_links
from parser import saver

if __name__ == '__main__':
    store_address = 'https://gastronomia.by'
    html = get_url(store_address).text
    information_in_the_tag = get_tag_content(html, 'li', class_="menu-item")
    all_attribute_values = get_attribute_value(information_in_the_tag, 'a', 'href')
    all_full_links_from_catalog = get_full_links(store_address, all_attribute_values)
    all_pictures = saver(all_full_links_from_catalog, store_address)
