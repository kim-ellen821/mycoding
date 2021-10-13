dx = [0, -1, 0, 1]
dy = [-1, 0, 1, 0]

def clean(r, c, d):
    x = r
    y = c
    count = 1
    board[x][y]=2
    while True:
        t= d
        for _ in range(4):
            nx = x + dx[t]
            ny = y + dy[t]
            empty = 0
            #로봇의 방향을 바꾼 뒤 update
            t= (t+3) % 4
            if(0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0):
                #칸이 범위 내에 있고 벽이 아니라면
                board[nx][ny]=2
                empty = 1
                count += 1
                x = nx
                y = ny
                d = t
                break
        #
        if empty == 0:
            x += dx[d]
            y += dy[d]

            if board[x][y]==1: break
    return count

n, m = map(int, input().split())
r, c, d = map(int, input().split())

board = []
for i in range(n):
    board.append(list(map(int, input().split())))

ans =clean(r,c,d)
print(ans)