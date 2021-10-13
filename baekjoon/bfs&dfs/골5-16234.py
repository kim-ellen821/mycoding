dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

from collections import deque

n, l, r = map(int, input().split())
board = [0] * n
for i in range(n):
  board[i] = list(map(int, input().split()))
#print(board[0][0], board[1][0])
q = deque()
def bfs(i, j):
    visit[i][j]=True
    q.append((i, j))
    team.append([i, j])
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n and not visit[ny][nx]:
                if l <= abs(board[y][x]-board[ny][nx]) <= r:
                    q.append((ny, nx))
                    team.append([ny, nx])
                    visit[ny][nx] = True

def avg(team):
    val = 0
    for place in team:
        y, x = place
        val += board[y][x]
    val = val // len(team)
    for place in team:
        y, x = place
        board[y][x] = val

count = 0
team = []
while True:
    check = False
    visit = [[False] * n for _ in range((n))]
    for i in range(n):
        for j in range(n):
            if visit[i][j]==False:
                team.clear()
                bfs(i, j)
                if len(team)>1:
                    check = True
                    avg(team)
    if check:
        count += 1                   
    else:
        break
print(count)