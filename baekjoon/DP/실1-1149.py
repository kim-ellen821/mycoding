N = int(input())

prices = [list(map(int, input().split())) for _ in range(N)]
small = [[0] * 3 for _ in range(N)]

for i in range(3):
    small[0][i] = prices[0][i]
for i in range(1, N):
    small[i][0] = min(small[i-1][1], small[i-1][2]) + prices[i][0]
    small[i][1] = min(small[i-1][0], small[i-1][2]) + prices[i][1]
    small[i][2] = min(small[i-1][0], small[i-1][1]) + prices[i][2]
print(min(small[N-1]))