n, m = map(int, input().split())
board = [[] for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, input().split()))

print(board)