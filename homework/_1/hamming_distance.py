import math
import random


LEN_OF_WORDS = 5
CHAR_SEQUENCE = 'aAbBcCdDeEfFgGhHiIjJkKlLmMnNoOpPqQrRsStTuUvVwWxXyYzZ'
WORDS_QUANTITY = 10000


def generate_word():
    word = ''
    for i in range(LEN_OF_WORDS):
        word += CHAR_SEQUENCE[random.randint(0, len(CHAR_SEQUENCE) - 1)]
    return word


def generate_list_of_words(words_quantity):
    words_list = []
    for i in range(words_quantity):
        words_list.append(generate_word())
    return words_list


def cross_words(word_1, word_2):
    coefficient_1 = random.randint(0, LEN_OF_WORDS - 1)
    coefficient_2 = random.randint(0, LEN_OF_WORDS - 1)
    result = word_1[:coefficient_1] + word_2[coefficient_2] + word_1[(coefficient_1 + 1):]
    return result


def make_next_generation(words_list):
    for i in range(WORDS_QUANTITY):
        words_list[i] = cross_words(words_list[i], words_list[WORDS_QUANTITY - i - 1])
    return words_list


def compare_words(word_1, word_2):
    compare_value = 0
    for i in range(LEN_OF_WORDS):
        compare_value += math.fabs(CHAR_SEQUENCE.index(word_1[i]) - CHAR_SEQUENCE.index(word_2[i]))
    return compare_value


def fitness_function(word_list, best_word):
    max_coincidence = 0
    min_coincidence = compare_words(word_list[0], best_word)
    closest_word = ''
    for i in range(WORDS_QUANTITY):
        compare_value = compare_words(word_list[i], best_word)
        if max_coincidence < compare_value:
            max_coincidence = compare_value
        if min_coincidence > compare_value:
            min_coincidence = compare_value
            closest_word = word_list[i]
    return [max_coincidence, min_coincidence, closest_word]


ideal_word = generate_word()
print('Ideal word: ' + ideal_word)

for y in range(10000):
    list_of_words = generate_list_of_words(WORDS_QUANTITY)
    for x in range(40):
        list_of_words = make_next_generation(list_of_words)
        p = fitness_function(list_of_words, ideal_word)
        if p[1] < 5.0:
            print(p)
