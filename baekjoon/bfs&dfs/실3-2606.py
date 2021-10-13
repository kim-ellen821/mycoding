# count = 0

# def dfs(start):
#     if not visited[start]:
#         visited[start] = True
#         global count
#         count += 1
#         for i in graph[start]:
#             dfs(i)

# edge = int(input())
# node = int(input())

# graph = [[] for _ in range(edge + 1)]# for _ in range(edge)]
# visited = [False] * (edge + 1)

# for _ in range(node):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# dfs(1)
# print(count - 1)
from collections import deque

def bfs(start):
    count = 0
    q = deque()
    visited[start] = True
    for i in graph[start]:
        q.append(i)
    while q:
        s = q.popleft()
        if not visited[s]:
            visited[s] = True
            count += 1
            for i in graph[s]:
                q.append(i)
    return count


edge = int(input())
node = int(input())

graph = [[] for _ in range(edge + 1)]# for _ in range(edge)]
visited = [False] * (edge + 1)

for _ in range(node):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

answer = bfs(1)
print(answer)