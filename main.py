import requests
from bs4 import BeautifulSoup


def get_url(url):
    """takes url as an argument, returns the response in html format"""
    response = requests.get(url)
    return response.text


def catalog(html, first_tag, second_tag, what_to_take, address, class_="menu-item"):
    """gets an html document as an argument,
     returns all links to products in the catalog"""
    soup = BeautifulSoup(html, 'lxml')
    store_catalog = soup.find_all(first_tag, class_)
    all_product_links = []
    for every_element in store_catalog:
        href = every_element.find(second_tag).get(what_to_take)
        full_product_link = address + href
        all_product_links.append(full_product_link)
    return all_product_links


html_text = get_url('https://gastronomia.by')
result = catalog(html_text, 'li', 'a', 'href', 'https://gastronomia.by')
print(result)
