string = input('Enter your string:\n')
num_om_chars = []
chars = []

for i in range(len(string)):
    if string[i] in chars:
        num_om_chars[chars.index(string[i])] += 1
    else:
        chars.append(string[i])
        num_om_chars.append(1)

for i in range(len(num_om_chars)):
    print('\"' + str(chars[i]) + "\' - " + str(num_om_chars[i]))
