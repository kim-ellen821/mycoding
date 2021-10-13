from collections import deque

q = deque([])
n = int(input())
for i in range(1, n+1):
    q.append(i)
print

for _ in range(n - 1):
    f = q.popleft()
    s = q.popleft()
    q.append(s)

ans = q.pop()
print(ans)