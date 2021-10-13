def isTrue(x):
    for i in range(x):
        if board[x] == board[i] or abs(board[x] - board[i]) == x - i:
            return False
    return True

def dfs(cnt):
    global count
    if cnt == N:
        count += 1
    else:
        for i in range(N):
            board[cnt] = i
            if isTrue(cnt):
                dfs(cnt + 1)

N = int(input())
board = [0] * N
count = 0
dfs(0)
print(count)