n = int(input())
arr = [[0]*10 for _ in range(101)]
for i in range(1, 10):
    arr[0][i] = 1

for i in range(1, n):
    for j in range(10):
        if j == 0:
            arr[i][j] = arr[i-1][1]
        elif j == 9:
            arr[i][j] = arr[i-1][8]
        else:
            arr[i][j] = arr[i-1][j-1] + arr[i-1][j+1]
print(sum(arr[n-1]) % 1000000000)

# import sys
# # sys.stdin=open('input.txt')
# from collections import deque
# mod = 10**9

# N=int(sys.stdin.readline())
# mm=[[0]*10 for _ in range(N+2)]
# mm[1]=[0,1,1,1,1,1,1,1,1,1]

# for i in range(2,N+1):
#     mm[i][0] = mm[i-1][1]
#     mm[i][9] = mm[i-1][8]
#     for j in range(1,9):
#         mm[i][j] = mm[i-1][j-1]+mm[i-1][j+1]

# print(mm)
# print(sum(mm[N])%mod)