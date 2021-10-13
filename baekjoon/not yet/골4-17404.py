n = int(input())
cost = [[] for _ in range(n)]


for i in range(n):
    cost[i] = list(map(int, input().split()))
# for i in range(3):
#     tot[i*2], tot[i*2 + 1] = cost[0][i], cost[0][i]
# print(cost)
# print(tot)

# for i in range(1, n):
#     if i%3 == 0:
