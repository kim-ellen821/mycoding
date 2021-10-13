#### wrong dfs code ######
# import sys
# sys.setrecursionlimit(10000)
# m, n, k = map(int, input().split())
# board = [[0]* n for _ in range(m)]

# for i in range(k):
#     lx, ly, rx, ry = map(int, input().split())
#     for i in range(ly, ry):
#         for j in range(lx, rx):
#             board[i][j] = 1

# def dfs(y, x):
#     if 0 <= x < m and 0 <= y < n:
#         if board[y][x] == 0:
#             global count
#             count += 1
#             board[y][x] = 2
#             dfs(y, x+1)
#             dfs(y, x-1)
#             dfs(y+1, x)
#             dfs(y-1, x)
#     return count
    
# num = 0
# sizes = []
# for i in range(m):
#     for j in range(n):
#         if board[i][j] == 0:
#             count = 0
#             dfs(i, j)
#             sizes.append()

# print(len(sizes))
# sizes.sort()
# for i in range(len(sizes)):
#     print(sizes[i], end=' ')
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
import sys
from collections import deque

m, n, k = map(int, input().split())
board = [[0]* n for _ in range(m)]

for i in range(k):
    lx, ly, rx, ry = map(int, input().split())
    for i in range(ly, ry):
        for j in range(lx, rx):
            board[i][j] = 1

print(board)

q = deque()

def bfs(i, j):
    q.append([i, j])
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and board[ny][nx] == 0:
                board[ny][nx] = 2
                global count
                count += 1
                q.append([ny, nx])


sizes = []
for i in range(m):
    for j in range(n):
        if board[i][j] == 0:
            count = 1
            board[i][j]=2
            bfs(i, j)
            sizes.append(count)

print(len(sizes))
sizes.sort()
for i in range(len(sizes)):
    print(sizes[i], end=' ')