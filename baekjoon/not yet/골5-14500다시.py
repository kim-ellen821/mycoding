import sys; input = sys.stdin.readline
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
moves = [[(0,1),(0,2),(1,1)], [(0,1),(0,2),(1,-1)], [(1,0),(2,0),(1,1)], [(1,0),(2,0),(1,-1)]]
big = -1

def check(x, y):
    for move in moves:
        try:
            tmp = board[x][y] + board[x+move[0][0]][y+move[0][1]] + board[x+move[1][0]][y+move[1][1]] + board[x+move[2][0]][y+move[2][1]]
        except:
            tmp = 0
    global big
    big = max(tmp, big)            

def morel(x, y, cnt, val):
    if cnt == 4:
        global big
        big = max(big, val)
        return
    else:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M and not visit[nx][ny]:
                visit[nx][ny] = True
                morel(nx, ny, cnt +1, val + board[nx][ny])
                visit[nx][ny] = False

N, M = map(int, input().split())
board = [[] for _ in range(N)]
visit = [[False] * M for _ in range(N)]


for i in range(N):
    board[i] = list(map(int, input().split()))


for i in range(N):
    for j in range(M):
        visit[i][j] = True
        morel(i, j, 1, board[i][j])
        visit[i][j]=False
        check(i, j)
print(big)