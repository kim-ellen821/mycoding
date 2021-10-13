from collections import deque

n = int(input())

for _ in range(n):
    sentence = input()
    check = []
    VPS = False
    for i in range(len(sentence)):
        check.append(sentence[i])
    q = deque()
    for i in check:
        if i == '(':
            q.append(i)
        else:
            if len(q) == 0:
                q.append(i)
                break
            else:
                q.pop()
    if len(q) == 0:
        VPS = True


    if VPS:
        print('YES')
    else:
        print('NO')
