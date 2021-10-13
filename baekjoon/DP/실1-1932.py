n = int(input())
tri = [[] * 1 for _ in range(n)]
cost = [[] * 1 for _ in range(n)]

for i in range(n):
    tri[i] = list(map(int, input().split()))

cost[0].append(tri[0][0])
for i in range(1, n):
    for j in range(0, i + 1):
        if j == 0:
            cost[i].append(cost[i-1][0] + tri[i][0])
        elif 1 <= j < i:
            cost[i].append(max(cost[i-1][j-1], cost[i-1][j]) + tri[i][j])
        else:
            cost[i].append(cost[i-1][j-1] + tri[i][j])
print(max(cost[n-1]))