dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N = int(input())
board = [[] for _ in range(N)]
for i in range(N):
    tmp = input()
    for j in range(N):
        board[i].append(tmp[j])

print(board)
def change(x, y, now):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<N and 0<=ny<N and board[nx][ny] == now:
            return True
    return False
big = 0
changed = False
for i in range(N):
    count, now = 1, board[i][0]
    for j in range(1, N):
        if j == N-1:
            big = max(big, count)
            break
        if board[i][j] == now: 
            count+=1
            print('same',i,j,count)
        else:
            if changed:
                count = 1
                big = max(big, count)
                now = board[i][j]
            else:
                if change(i, j, now):
                    count +=1
                    changed = True
                    print('no change',i, j, count)
                else:
                    big = max(big, count)
                    count = 1
                    now = board[i][j]
                    print('change', i, j, big)
    

# for i in range(N):
#     count, now = 0, board[i][0]
#     for j in range(1, N):
#         if board[j][i] == now: count+=1
#         else:
#             if change(j, i, now):
#                 count +=1
#             else:
#                 big = max(big, count) 
#                 count = 1
#                 now = board[j][i]
print(big)