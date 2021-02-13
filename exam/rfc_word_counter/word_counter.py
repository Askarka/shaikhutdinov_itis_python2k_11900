import re

RFC_FROM_NUM = 1
RFC_TO_NUM = 100
FIRST_RFC_PUB_YEAR = 1969
CURRENT_YEAR = 2021
MAX_OUT_STAR_WIDTH = 60

array_of_words_num_in_years = []
for i in range(FIRST_RFC_PUB_YEAR, CURRENT_YEAR + 1):
    array_of_words_num_in_years.append(0)

for i in range(RFC_FROM_NUM, RFC_TO_NUM + 1):
    rfc_file = open('rfc_files/rfc' + str(i) + '.txt')
    rfc_file_text = rfc_file.read()
    search_result_object = re.search(r'1969|19[7-9]\d|20[0-1]\d|202[01]', rfc_file_text)
    if search_result_object:
        words_in_rfc = len(re.findall(r'[\w-]+', rfc_file_text))
        # print(i, search_result_object.group(), words_in_rfc)
        array_of_words_num_in_years[int(search_result_object.group()) - 1969] += words_in_rfc

max_words_value = max(array_of_words_num_in_years)

stars_num = 0
star_string = '*'
# print(array_of_words_num_in_years)

for i in range(FIRST_RFC_PUB_YEAR, CURRENT_YEAR + 1):
    stars_num = (array_of_words_num_in_years[i - 1969] * 60) // max_words_value
    if stars_num != 0:
        print(str(FIRST_RFC_PUB_YEAR + i - 1969) + ': ' + str(star_string * stars_num))
