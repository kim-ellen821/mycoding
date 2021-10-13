s = input().rstrip('\n')
words = [''] * len(s)
words[0] = s

for i in range(1, len(s)):
    tmp = s[i:len(s)]
    words[i] = tmp
words.sort()
for i in range(len(words)):
    print(words[i])