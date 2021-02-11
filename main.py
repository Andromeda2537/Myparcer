from funk import get_url
from funk import catalog
from parser import saver


if __name__ == '__main__':
    html_text = get_url('https://gastronomia.by').text
    all_product = catalog(html_text, 'li', 'a', 'href', 'https://gastronomia.by')
    result = saver(all_product)
