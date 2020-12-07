import random


def convert_dec_to_binary(dec_num):
    res_list = []
    if dec_num == 0:
        return '0'
    while dec_num != 0:
        if dec_num % 2 == 1:
            res_list.insert(0, '1')
        else:
            res_list.insert(0, '0')
        dec_num = dec_num // 2
    return ''.join(res_list)


def to_bin_decorator(func):
    def wrapper():
        return convert_dec_to_binary(func())

    return wrapper


@to_bin_decorator
def create_number(min_val=0, max_val=1000):
    return random.randint(min_val, max_val)


print(create_number())
