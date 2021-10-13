N, K = map(int, input().split())

#dp = [[0] * (N+1) for _ in range(K+1)]
dp = [[0] * (10) for _ in range(10)]
for i in range(N+1):
    dp[1][i] = 1
# for i in range(1, K+1):
#     dp[i][0] = 1

for i in range(1, K+1):
    for j in range(N+1):
        for k in range(i+1):
            dp[i][j] += dp[k][j-1]
        dp[i][j] %= int(1e9)
print(dp)
print(dp[K][N])