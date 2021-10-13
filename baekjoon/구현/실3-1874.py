import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
q = deque()
flag = 0
visit = [False] * (n + 1)
stack = True
#print(visit)
for _ in range(n):
    x = int(input())
    if len(q) == 0:
        for _ in range(x):
            q.append('+')
        q.append('-')
        flag = x
        visit[x] = True
        #print(q)
    else:
        if visit[x]:
            print('NO')
            stack = False
            break
        if flag < x:
            for i in range(flag, x + 1):
                if not visit[i]:
                    q.append('+')
            q.append('-')
            visit[x] = True
            flag = x
            # print('작을 때')
            # print(q)
        elif flag > x:
            for i in range(flag, x  - 1, -1):
                if not visit[i]:
                    q.append('-')
                    visit[i] = True
                    flag = x
            # print('bigger')
            # print(q)
if stack:
    for _ in range(len(q)):
        print(q.popleft())
