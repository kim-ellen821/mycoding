import sys
from collections import deque

input = sys.stdin.readline
n = int(input())
q = deque()
for _ in range(n):
    cmd = input().split()
    
    if cmd[0] == 'push_back':
        q.append(int(cmd[1]))
    elif cmd[0] == 'push_front':
        q.appendleft(int(cmd[1]))
    elif cmd[0] == 'pop_front':
        if(len(q)>=1):
            front = q.popleft()
            print(front)
        else: print(-1)
    elif cmd[0] == 'pop_back':
        if(len(q)>=1):
            back = q.pop()
            print(back)
        else: print(-1)
    elif cmd[0] == 'size':
        print(len(q))
    elif cmd[0] == 'empty':
        if len(q) == 0:
            print(1)
        else:
            print(0)
    elif cmd[0] == 'front':
        if len(q)==0:
            print(-1)
        else:
            front = q.popleft()
            print(front)
            q.appendleft(front)
    elif cmd[0] =='back':
        if len(q) == 0:
            print(-1)
        else:
            back = q.pop()
            print(back)
            q.append(back)