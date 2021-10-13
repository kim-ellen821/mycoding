n = int(input())
arr = [[] for _ in range(200001)]

for _ in range(n):
    x, y = map(int, input().split())
    y += 100000
    arr[y].append(x)
    if len(arr[y])>1:
        arr[y].sort()

for i in range(200001):
    if len(arr[i])>=1:
        for j in range(len(arr[i])):
            print(arr[i][j], i - 100000)