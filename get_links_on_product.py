import requests
from bs4 import BeautifulSoup


def get_url(url):
    """takes url as an argument, returns the response"""
    response = requests.get(url)
    return response


def get_tag_content(html_text, tag, class_="menu-item"):
    """Searches the html tree, returns the information contained
    in the tag with the corresponding identifier"""
    soup = BeautifulSoup(html_text, 'lxml')
    tags_content = soup.find_all(tag, class_)
    return tags_content


def get_attribute_value(tags_content, tag, tag_attribute):
    """Searches for the specified tag in previously sorted tags and
     gets it as an attribute value.Returns a list of attribute values"""
    attribute_values = []
    for element in tags_content:
        link_to_section = element.find(tag).get(tag_attribute)
        attribute_values.append(link_to_section)
    return attribute_values


def get_full_links(address, attribute_values):
    """Returns a full link to a directory section"""
    all_full_link = []
    for link in attribute_values:
        full_link = address + link
        all_full_link.append(full_link)
    return all_full_link


def get_src(full_link):
    """Accepts links to product from the catalog
     as an argument and returns links to images"""
    html = get_url(full_link).text
    tag_a = get_tag_content(html, 'a', class_="thumb shine")
    src = get_attribute_value(tag_a, 'img', 'src')
    return src
