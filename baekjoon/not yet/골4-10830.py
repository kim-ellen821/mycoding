# def rotate(board):
#     n = len(board)
#     arr = [[0] * n for _ in range(n)]
#     for i in range(n):
#         for j in range(n):
#             arr[j][n-i-1] = board[i][j]
#     return arr

# n, b = map(int, input().split())
# board = [[]for _ in range(n)]


# for i in range(n):
#     board[i]=list(map(int, input().split()))

# arr = [[0] * n for _ in range(n)]
# tmparr = [[0] * n for _ in range(n)]
# tmp = rotate(board)
# for t in range(1, b):   
#     for i in range(n):
#         for j in range(n):
#             val = 0
#             if t == 1:
#                 for k in range(n):
#                     #print(board[i][k], end=' * ')
#                     #print(tmp[j][n - k - 1])
#                     val += (board[i][k] * tmp[j][n - k - 1]) % 1000
#                 tmparr[i][j] += val
#             else:
#                 for k in range(n):
#                     val += (arr[i][k] * tmp[j][n - k - 1]) % 1000
#                 tmparr[i][j] = val%1000

#     ##여기서 arr = tmparr하면 바로 값이 update되는데 이유를 모르겠음
#     for i in range(n):
#         for j in range(n):
#             arr[i][j] = tmparr[i][j]
# for i in range(n):
#     for j in range(n):
#         print(arr[i][j], end = ' ')
#     print()
def rotate(board):
    n = len(board)
    arr = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            arr[j][n-i-1] = board[i][j]
    return arr

n, b = map(int, input().split())
board = [[]for _ in range(n)]

for i in range(n):
    board[i]=list(map(int, input().split()))

arr = [[0] * n for _ in range(n)]
tmparr = [[0] * n for _ in range(n)]
tmp = rotate(board)
for t in range(1, b):   
    for i in range(n):
        for j in range(n):
            val = 0
            if t == 1:
                for k in range(n):
                    val += (board[i][k] * tmp[j][n - k - 1]) % 1000
                tmparr[i][j] += val
            else:
                for k in range(n):
                    val += (arr[i][k] * tmp[j][n - k - 1]) % 1000
                tmparr[i][j] = val%1000
    for i in range(n):
        for j in range(n):
            arr[i][j] = tmparr[i][j]
            
for i in range(n):
    for j in range(n):
        print(arr[i][j], end = ' ')
    print()
