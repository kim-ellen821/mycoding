n = int(input())
up = [[0] * 10 for _ in range(1001)]
for i in range(10):
    up[0][i] = 1
# for i in range(10):
#     up[1][i] = i+1  
# for i in range(2, n):
#     for j in range(10):
#         num = up[i-1][j]
#         up[i][j] = ((num) * (num+1) // 2)
# print(sum(up[n-1]) % 10007)
for i in range(1, n):
    for j in range(10):
        for k in range(j, 10):
            up[i][j] += up[i-1][k]

print(sum(up[n-1]) % 10007)