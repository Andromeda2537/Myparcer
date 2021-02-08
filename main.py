import requests
from bs4 import BeautifulSoup
import os
# from multiprocessing import Pool


def get_url(url):
    """response in html format"""
    response = requests.get(url)
    return response.text


def find_all_links(html):
    """links to all products"""
    soup = BeautifulSoup(html, 'lxml')
    links = soup.find_all('a', class_="thumb shine")
    all_scr = []
    for link in links:
        scr = link.find('img').get('src')
        a = 'https://gastronomia.by' + scr
        all_scr.append(a)
    return all_scr


def save_pictures(all_scr):
    images_path = 'images'
    if not os.path.exists(images_path):
        os.makedirs(images_path)
    with open(images_path + "/gastronomia.jpg", 'ab+') as f:
        for i in all_scr:
            jpg = requests.get(i).content
            f.write(jpg)
    return


print(save_pictures(find_all_links(get_url('https://gastronomia.by/catalog/svezhaya_vypechka/khleb'))))
