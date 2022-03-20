import time

import requests

SITE_1 = 'https://yandex.ru/'
SITE_2 = 'http://core.uenv.ru/'
SITE_3 = 'http://xp_sch/'


def create_sites_list():
    print('Enter the number of sites for check: ')
    site_tum = input()
    print('Enter the sites url via enter:')
    for i in range(int(site_tum)):
        url = input()
        return array_of_sites_urls.append(url)


def check_site(sites_url):
    resp = requests.get(sites_url)
    print(resp.status_code)
    # return message


array_of_sites_urls = [SITE_1, SITE_2, SITE_3]

for site_url in array_of_sites_urls:
    message = check_site(site_url)
    # print(message.status_code)

timing = time.time()
running = True
while running:
    if time.time() - timing > 30.0:
        timing = time.time()

        for site_url in array_of_sites_urls:
            message = check_site(site_url)
            # print(message.status_code)
# array_of_sites_urls = create_sites_list()
