string = input().rstrip('\n')

for word in string:
    tmp = ord(word) + 13
    if 65 <= ord(word) <=90:
        if tmp > 90:
            tmp -= 26
    elif 97 <= ord(word) <=122:
        if tmp > 122:
            tmp -= 26
    else:
        tmp -= 13
    print(chr(tmp), end='')