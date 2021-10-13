import heapq
n = int(input())

def findmin(arr):
    loc = []
    q = []
    for i in range(len(arr)):
        heapq.heappush(q,(arr[i], i))
    for _ in range(len(arr)):
        x, index = heapq.heappop(q)
        loc.append(index)
    return loc


a = list(map(int, input().split()))
b = list(map(int, input().split()))
loc = []
sum = 0
loc = findmin(b)
a.sort(reverse = True)
for i in range(len(a)):
    sum += a[i] * b[loc[i]]
print(sum)