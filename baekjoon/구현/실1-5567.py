n = int(input())
m = int(input())

def find(friend):
    for i in graph[friend]:
        if not friend2[i]:
            friend2[i] = True

graph = [[] for _ in range(n + 1)]
friend = [False] * (n + 1)
friend[1] = True
friend2 = [False] * (n + 1)
friend2[1] = True

ans = 0
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
 
if len(graph[1]) != 0:
    for i in graph[1]:
        friend[i] = True
        find(i)

for i in range(2, n + 1):
    if friend[i]==True or friend2[i] == True:
        ans += 1
print(ans)