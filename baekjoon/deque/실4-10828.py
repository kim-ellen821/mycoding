import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
q = deque()
for _ in range(n):
    do = input().strip()
    if do[0] == 'p':
        if do[1] == 'u':
            tmp = do[5:len(do) + 1]
            q.append(int(tmp))
        elif do[1] == 'o':
            if len(q) == 0:
                print(-1)
            else:
                print(q.pop())
    elif do[0] == 's':
        print(len(q))
    elif do[0] == 'e':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif do[0] =='t':
        if len(q) == 0:
            print(-1)
        else:
            tmp = q.pop()
            print(tmp)
            q.append(tmp)