maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]
#maps = [[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

from collections import deque

def solution(maps):
    answer = 0
    r = len(maps)
    c = len(maps[0])
    q = deque()
    q.append((0,0))
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<r and 0<=ny<c and maps[nx][ny]==1:
                maps[nx][ny] = maps[x][y] + 1
                q.append((nx, ny))
    if maps[r-1][c-1] == 1:
        answer = -1
    else: 
        answer = maps[r-1][c-1]
    return answer

ans = solution(maps)
print(ans)