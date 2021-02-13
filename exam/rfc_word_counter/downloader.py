import requests

URL = 'https://www.rfc-editor.org/rfc/'
RFC_FROM_NUM = 1
RFC_TO_NUM = 100

for i in range(RFC_FROM_NUM, RFC_TO_NUM + 1):
    resp = requests.get(URL + 'rfc' + str(i) + '.txt')
    file = open('rfc_files/rfc' + str(i) + '.txt', 'w')
    file.write(resp.text)
