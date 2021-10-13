dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

def dfs(x, y):
    go = True
    val = board[x][y]
    global count
    for i in range(4):
        nx = x + val * dx[i]
        ny = y + val * dy[i]
        if nx!= 0 and 0<=nx<n:
            for i in range(nx):
                if board[nx][ny] == 'H':
                    go = False
        elif ny!= 0 and 0<=ny<m:
            for i in range(nx):
                if board[nx][ny] == 'H':
                    go = False
    if go and count < n * m:
        count = +1
        dfs(nx, ny)
    else:
        count = -1

n, m = map(int, input().split())
count  = 0
board = [[] for _ in range(n)]
for i in range(n):
    line = input()
    for j in range(m):
        board[i].append(int(line[j]))
#print(board)
dfs(0,0)
print(count)