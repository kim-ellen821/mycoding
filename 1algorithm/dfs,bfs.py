from collections import deque

def dfs(graph, visit, s):
    visit[s]=True
    print(s, end=' ')
    for i in graph[s]:
        if not visit[i]:
            dfs(graph, visit,i)

def bfs(graph, visit, s):
    q = deque([s])
    visit[s] = True
    while q:
        front = q.popleft()
        print(front, end=" ")
        for i in graph[front]:
            if not visit[i]:
                q.append(i)
                visit[i]=True


graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False] * 9

dfs(graph, visited, 1)
bfs(graph, visited, 1)