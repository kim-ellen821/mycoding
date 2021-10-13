# from collections import deque
# n, m = map(int, input().split())
# graph = [[] for _ in range(n + 1)]
# visited = [False] * (n + 1)
# count = 0

# def dfs(start):
#     global count
#     visited[start]=True
#     for j in graph[start]:
#         if not visited[j]:
#             print('탐색',end=' ')
#             print(j)
#             dfs(j)

# for _ in range(m):
#     a, b = map(int, input().split())
#     graph[a].append(b)
#     graph[b].append(a)

# for i in range(1, n+1):
#     if not visited[i]:
#         print('시작:',end='')
#         print(i)
#         check = dfs(i)
#         count+=1

# print(count)


import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline
n, m  = map(int, input().split())
board = [[] for _ in range(n+1)]
visited = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    board[a].append(b)
    board[b].append(a)

def find(start):
    #print(start)
    visited[start] = True
    for j in board[start]:
        if not visited[j]:
            print('탐색:',end='')
            print(j)
            find(j)
    return

count = 0
for i in range(1, n+1):
    if not visited[i]:
        print('new:',end='')
        print(i)
        find(i)
        count += 1
print(count)