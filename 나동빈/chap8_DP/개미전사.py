
N = int(input())
arr= list(map(int, input().split()))

cost = [0] * N

cost[0] = arr[0]

cost[1] = max(arr[0], arr[1])

for i in range(2, N):
    cost[i] = max(cost[i - 2]+arr[i], cost[i - 1])

print(cost[N - 1])