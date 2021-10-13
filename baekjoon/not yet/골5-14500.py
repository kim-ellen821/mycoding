dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
moves = [[[0, 1],[0,2],[1,1]], [[0, 1],[0,2],[-1,1]],
[[1,0],[2,0],[1,1]], [[1,0],[2,0],[1,-1]]]

n, m = map(int, input().split())
board = [list(map(int, input().split())) for _ in range(n)]
visit = [[False] * m for _ in range(n)]
big = -1
def dfs(x, y, cnt, ans):
    if cnt == 4:
        global big
        big = max(big, ans)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and not visit[nx][ny]:
                visit[nx][ny] = True
                dfs(nx, ny, cnt+1, ans+board[nx][ny])
                visit[nx][ny] = False
def check(x, y):
    global big
    for i in moves:
        try: ans = board[x][y] + board[x + i[0][0]][y + i[0][1]] + board[x + i[1][0]][y + i[1][1]] + board[x + i[2][0]][y + i[2][1]]
        except: ans = 0
        big = max(big, ans)

for i in range(n):
    for j in range(m):
        visit[i][j] = True
        dfs(i,j, 1, board[i][j])
        visit[i][j] = False
        check(i,j)
print(big)