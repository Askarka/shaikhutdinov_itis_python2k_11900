string_to_scan = input('Enter your string:\n')
array_of_vowels = ['a', 'e', 'y', 'u', 'i', 'o']
num_of_vowels = 0
for i in string_to_scan:
    for j in array_of_vowels:
        if i == j:
            num_of_vowels+=1
print('Number of vowels is ' + str(num_of_vowels) + '.')