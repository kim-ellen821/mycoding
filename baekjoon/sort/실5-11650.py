import sys
input = sys.stdin.readline
arr = [[] for _ in range(200001)]
n = int(input())
for i in range(n):
    x, y = map(int, input().split())
    arr[x + 100000].append(y)
    #print(arr[x+100000])
    if len(arr[x + 100000])!=0:
        arr[x + 100000].sort()
for i in range(200001):
    #for j in range(len(i)):
    if len(arr[i])!= 0:
        for j in range(len(arr[i])):
            print(i-100000, arr[i][j])