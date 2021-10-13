INF = int(1e9)
def solution(N, road, K):
    answer = 0
    board = [[INF] * (N + 1) for _ in range(N + 1)]
    for i in range(N+1):
        board[i][i] = 0
    for x in road:
        a, b, c = x[0], x[1], x[2]
        if board[a][b] == INF:
            board[a][b], board[b][a] = c, c
        else:
            small = min(board[a][b], c)
            board[a][b], board[b][a] = small, small
    for i in range(1, N + 1):
        for j in range(1, N + 1):
            for k in range(1, N + 1):
                board[i][j] = min(board[i][j], board[i][k] + board[k][j])
    print(board)
    for i in range(1, N+1):
        if board[1][i] <= K:
            answer += 1
    return answer