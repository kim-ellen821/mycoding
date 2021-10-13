
n, m = map(int, input().split())

graph = [[] for _ in range(n)]
board = [[0]* n for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))
x, y = map(int, input().split)



