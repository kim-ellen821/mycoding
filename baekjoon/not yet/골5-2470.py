# import heapq
# n = int(input())
# q=[]
# arr = list(map(int, input().split()))
# for j in arr:
#     heapq.heappush(q, j)
# print(q)
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
print(arr)
for i in range(n):
    for j in range(n-1, 1, -1):
        