def find(n):
    if n < 0 : return 100000
    if cost[n] != 0:
        return cost[n]
    temp =[]
    for x in arr:
        temp.append(1 + find(n - x))
    return min(temp)

n, m = map(int, input().split())
arr = [0] * n
cost = [0] * 10001
for i in range(n):
    arr[i]= int(input())
for x in arr:
    cost[x] = 1

arr.sort()
count = find(m)
if count > 100000 : count = -1
print(count)