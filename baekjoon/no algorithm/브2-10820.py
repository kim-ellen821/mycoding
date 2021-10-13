while True:
    try:
        sentence = input().rstrip('\n')
        count = [0] * 4
        for word in sentence:
            if ord(word) == 32:
                count[3] += 1
            elif 97 <= ord(word) <= 122:
                count[0] += 1
            elif 65 <= ord(word) <= 90:
                count[1] += 1
            elif 48 <= ord(word) <= 57:
                count[2] += 1

        for i in range(4):
            print(count[i], end = ' ')
    except EOFError:
        break
