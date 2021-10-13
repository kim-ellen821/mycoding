dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def change(r):
    if r == 0: return 3
    elif r == 1: return 0
    elif r == 2: return 1
    elif r == 3: return 2

n, m = map(int, input().split())
board =[[] for _ in range(n)]

def find(r,c,d):
    print('r, c, d:',end='')
    print(r,c,d)
    if 0<=r<n and 0<=c<m:
        if board[r][c] == 0:
            board[r][c] = 2
            global count
            count += 1
        #elif board[r][c] == 1:
            for i in range(4):
                nx = r + dx[d]
                ny = c + dy[d]
                t = change(d)
                if board[nx][ny] == 0:
                    print('회전')
                    find(nx, ny, t)
            print('후진')
            if r == 0: c -=1
            elif r == 1: r -= 1
            elif r == 2: c += 1
            else: r += 1
            # if board[r][c] == 1 or r<0 or r>=n or c<0 or c>=m:
            #     return count
            # elif board[r][c] == 0 and 0<=r<n and 0<=c<m:
            #     find(r,c,d)
            if board[r][c] == 1:
                return count
            else:
                find(r,c,d)
    return count
            

count = 0
r, c, d = map(int, input().split())
for i in range(n):
    board[i] = list(map(int, input().split()))
ans = find(r,c,d)
print(board)
print(ans)

# dx = [0, -1, 0, 1]
# dy = [-1, 0, 1, 0]

# def clean(r, c, d):
#     x = r
#     y = c
#     count = 1
#     board[x][y]=2
#     while True:
#         t= d
#         for _ in range(4):
#             nx = x + dx[t]
#             ny = y + dy[t]
#             empty = 0
#             t= (t+3) % 4
#             if(0 <= nx < n and 0 <= ny < m and board[nx][ny] == 0):
#                 board[nx][ny]=2
#                 empty = 1
#                 count += 1
#                 x = nx
#                 y = ny
#                 d = t
#                 break
#         if empty == 0:
#             if d == 0: x+=1
#             elif d == 1: y-=1
#             elif d ==2 : x -=1
#             elif d == 3: y+=1

#             if board[x][y]==1: break
#     return count

# n, m = map(int, input().split())
# r, c, d = map(int, input().split())

# board = []
# for i in range(n):
#     board.append(list(map(int, input().split())))

# ans =clean(r,c,d)
# print(board)
# print(ans)