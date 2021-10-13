# import sys
# input = sys.stdin.readline
# s = input().strip()
# alphabet = [0] * 26

# for w in s:
#     alphabet[ord(w) - 97] += 1

# for i in range(26):
#     print(alphabet[i], end=' ')

s = input().strip()
alphabet = [-1] * 26
for i in range(len(s)):
    if alphabet[ord(s[i]) - 97] == -1:
        alphabet[ord(s[i]) - 97] = i
for i in range(26):
    print(alphabet[i], end=' ')