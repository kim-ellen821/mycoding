MIN = -int(1e9)
n = int(input())
arr = list(map(int, input().split()))
dp = [MIN] * (100001)
dp2 = [MIN] * (100000)
dp[0] = arr[0]
for i in range(1, n):
    dp[i] = max(arr[i], arr[i]+ dp[i-1])
    dp2[i] = max(dp[i-1], dp2[i-1] + arr[i])
print(max(max(dp), max(dp2)))