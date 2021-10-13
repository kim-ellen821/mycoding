from collections import deque
k = int(input())
q = deque()
for _ in range(k):
    x = int(input())
    if x == 0 and len(q)>0:
        q.pop()
    else:
        q.append(x)
print(sum(q))