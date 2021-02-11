import requests
from bs4 import BeautifulSoup


def get_url(url):
    """takes url as an argument, returns the response"""
    response = requests.get(url)
    return response


def catalog(html, first_tag, second_tag, what_to_take, address, class_="menu-item"):
    """As an argument, it takes the necessary parameters for searching the soup:
    html text, tag and identifier, a tag for searching by the selected tag and
     an indication of the element to be removed,
      the resource address. returns a list of all products from the catalog"""
    soup = BeautifulSoup(html, 'lxml')
    store_catalog = soup.find_all(first_tag, class_)
    all_product_links = []
    for every_element in store_catalog:
        href = every_element.find(second_tag).get(what_to_take)
        full_product_link = address + href
        all_product_links.append(full_product_link)
    return all_product_links
