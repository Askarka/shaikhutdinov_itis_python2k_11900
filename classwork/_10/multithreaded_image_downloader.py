import multiprocessing
import os
import sys

import requests
import bs4


def find_pics(tree_of_tags):
    urls = []
    for image_tag in tree_of_tags.select('img'):
        if image_tag.get('src') == '':
            print('There an error...')
            sys.exit()
        elif image_tag.get('src')[0] == 'h':
            url_of_pic = image_tag.get('src')
        elif image_tag.get('src')[1] == '/':
            url_of_pic = 'https:' + image_tag.get('src')
        else:
            split_url = url.split('/')
            url_of_pic = split_url[0] + '//' + split_url[2] + image_tag.get('src')
        urls.append(url_of_pic)
    return tuple(urls)


def find_names(tree_of_tags):
    names = []
    for image_tag in tree_of_tags.select('img'):
        if image_tag.get('alt') is None:
            name_of_photo = ''
        else:
            name_of_photo = image_tag.get('alt')
        names.append(name_of_photo)
    return tuple(names)


def multiprocess_download(url_of_pic, name_of_pic):
    response_buffer = requests.get(url_of_pic)
    with open('images/' + name_of_pic + '_.png', 'wb') as file:
        for content in response_buffer.iter_content():
            file.write(content)


if __name__ == '__main__':
    url = 'https://www.fontanka.ru/2020/11/22/69566843/'
    # url = input('Enter your url: ')

    response = requests.get(url)
    response.raise_for_status()
    html = response.text
    tree = bs4.BeautifulSoup(html, 'html.parser')
    list_of_pics_src = find_pics(tree)
    # print(list_of_pics_src)
    list_of_names = find_names(tree)
    # print(list_of_names)
    if not os.path.exists("images"):
        os.mkdir("images")
    with multiprocessing.Pool() as pool:
        result = pool.starmap(multiprocess_download, zip(list_of_pics_src, list_of_names))
