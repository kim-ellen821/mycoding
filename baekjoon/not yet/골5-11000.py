import heapq

n = int(input())
q = []
for i in range(n):
    x,y  = (map(int, input().split()))
    heapq.heappush(q, (x, y))


print(q)