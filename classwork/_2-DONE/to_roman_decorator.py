import random


def convert_arab_to_roman(arab_num):
    roman_numerals = ("M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I")
    val_of_rom_num = (1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1)
    result = ''
    for i in range(13):
        while arab_num >= val_of_rom_num[i]:
            result += roman_numerals[i]
            arab_num -= val_of_rom_num[i]
    return result


def to_roman_decorator(func):
    def wrapper():
        return convert_arab_to_roman(func())

    return wrapper


@to_roman_decorator
def create_number(min_val=0, max_val=1000):
    return random.randint(min_val, max_val)


print(create_number())

'''
public class ArabToRomNumConverter {
    public static String convert(int x){
        String[] ch = {"M", "CM", "D", "CD", "C", "XC", "L", "XL", "X", "IX", "V", "IV", "I"};
        int[] n = {   1000,  900, 500,  400, 100,  90,  50,   40,  10,   9,    5,    4,    1};
        String res = "";
        for(int i = 0; i < 13; i++){
            while (x >= n[i]){
                res = res + ch[i];
                x -= n[i];
            }
        }
        return res;
    }
}
'''
