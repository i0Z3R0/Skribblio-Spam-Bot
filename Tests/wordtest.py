import re

possible = []
correctword = ' '
halfword = 'a___e'
wordlength = 5

f = open('wordlist.txt', 'r')
for line in f:
    if halfword != '':
        halfdot = halfword.replace("_", ".")
        print(halfdot)
        testword = line.strip('\n')
        if len(testword) == wordlength:
            reg = re.compile(halfdot)
            if bool(re.match(reg, testword)):
                possible.append(testword)
    else:
        if len(testword) == wordlength:
            possible.append(testword)

print(possible)
