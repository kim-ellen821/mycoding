def dfs(r, c):
    if r < 0 or r >= n or c < 0 or c >= m:
        return False
    if board[r][c] == 0:
        board[r][c] = 2
        dfs(r, c + 1)
        dfs(r, c - 1)
        dfs(r + 1, c)
        dfs(r - 1, c)
        return True
    return False

n, m = map(int, input().split())
board = []
for i in range(n):
    board.append(list(map(int, input().split())))

count = 0
for i in range(n):
    for j in range(m):
        check = dfs(i, j)
        if check == True:
            count += 1

print(count)