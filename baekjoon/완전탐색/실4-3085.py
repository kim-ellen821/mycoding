# dx1 = [1, 0, 0]
# dy1 = [0, 1, -1]
# dx2 = [-1, 1, 0]
# dy2 = [0 ,0, 1]

# N = int(input())
# board = [[] for _ in range(N)]
# for i in range(N):
#     tmp = input()
#     for j in range(N):
#         board[i].append(tmp[j])

# def change(x, y, now):
#     for i in range(3):
#         nx, ny = x+dx1[i], y+dy1[i]
#         if 0<=nx<N and 0<=ny<N and board[nx][ny] == now:
#             return True
#     return False
# def change2(x, y, now):
#     for i in range(3):
#         nx, ny = x+dx2[i], y+dy2[i]
#         if 0<=nx<N and 0<=ny<N and board[nx][ny] == now:
#             return True
#     return False
# big = 0
# changed = False
# for i in range(N):
#     count, now = 1, board[i][0]
#     for j in range(1, N):
#         if board[i][j] == now: 
#             count+=1
#             #print('same',i,j,count)
#         else:
#             if changed:
#                 count = 1
#                 big = max(big, count)
#                 now = board[i][j]
#                 changed = False
#             else:
#                 if change(i, j, now):
#                     count +=1
#                     changed = True
#                     #print('no change',i, j, count)
#                 else:
#                     big = max(big, count)
#                     count = 1
#                     now = board[i][j]
#                     #print('change', i, j, big)
#     big = max(big, count)

# changed = False
# for i in range(N):
#     count, now = 1, board[0][i]
#     print('first:', now)
#     for j in range(1, N):
#         if board[j][i] == now: 
#             count+=1
#             print('same',i,j,count)
#         else:
#             if changed:
#                 print('recount')
#                 count = 1
#                 big = max(big, count)
#                 now = board[j][i]
#                 changed = False
#             else:
#                 if change2(j, i, now):
#                     count +=1
#                     changed = True
#                     print('no change',i, j, count)
#                 else:
#                     big = max(big, count)
#                     count = 1
#                     now = board[j][i]
#                     print('change', i, j, big)
#     big = max(big, count)
# print(big)


def check(board):
    N = len(board)
    big = -1
    for i in range(N):
        count, now = 1, board[i][0]
        for j in range(1, N):
            if board[i][j] == now: 
                count+=1
            else:
                big = max(big, count)
                count, now = 1, board[i][j]
        big = max(big, count)
    for i in range(N):
        count, now = 1, board[0][i]
        for j in range(1, N):
            if board[j][i] == now: 
                count+=1
            else:
                big = max(big, count)
                count, now = 1, board[j][i]
        big = max(big, count)
    return big

N = int(input())
board = [[] for _ in range(N)]
for i in range(N):
    tmp = input()
    for j in range(N):
        board[i].append(tmp[j])
ans = 0
for i in range(N):
    for j in range(N-1):
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
        tmp = check(board)
        ans = max(ans, tmp)
        board[i][j], board[i][j+1] = board[i][j+1], board[i][j]
for i in range(N):
    for j in range(N-1):
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
        tmp = check(board)
        ans = max(ans, tmp)
        board[j][i], board[j+1][i] = board[j+1][i], board[j][i]
print(ans)