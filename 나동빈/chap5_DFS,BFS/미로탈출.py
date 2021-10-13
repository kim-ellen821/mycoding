#################미로 탈출 ###################################
from collections import deque

dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
def bfs(a, b):
    #count = 1
    q = deque()
    q.append((a, b))

    while q:
        x, y = q.popleft()
        
        print(str(x),str(y),':',board[x][y])
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and board[nx][ny] == 1:
                q.append((nx, ny))
                board[nx][ny] = board[x][y]+1
    return board[n-1][m-1]




n, m = map(int, input().split())
board =[]
for _ in range(n):
    board.append(list(map(int, input().split())))
ans = bfs(0,0)
print(ans)