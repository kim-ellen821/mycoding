import sys
input = sys.stdin.readline

arr = input()
check = False
tmp = ''

def flip(word, size):
    for i in range(len(word)):
        print(word[size - i - 1], end='')

for i in range(len(arr)):
    if not check:
        if arr[i]=='<':
            if len(tmp) > 0:
                flip(tmp, len(tmp))
                tmp =''
            print('<', end='')
            check = True
            continue
        elif 97<= ord(arr[i]) <= 122  or 48<= ord(arr[i]) <= 57:
            tmp += arr[i]
        elif arr[i]==' ':
            if len(tmp) > 0:
                flip(tmp, len(tmp))
                tmp =''
            print(end=' ')           
    elif check:
        if arr[i]=='>':
            check = False
            print(tmp, end='')
            print('>', end='')
            tmp=''
        else: 
            tmp += arr[i]
if len(tmp)>0:
    flip(tmp, len(tmp))