# data = [1,2,3,2,5]
# n = 5 #data 수
# m = 5#원하는 부분합
# start = 0
# end = 0
# partial_sum = 0
# count = 0
# for start in range(n):
#     while end < n and partial_sum < m:
#         partial_sum += data[end]
#         end += 1
#     if partial_sum == m:
#         count += 1
#     partial_sum-=data[start]
# print(count)

# import heapq
# import sys
# INF = int(1e9)
# input = sys.stdin.readline
# n, m = map(int, input().split())
# start = int(input())
# graph = [[] for _ in range(n + 1)]
# distance = [INF] * (n + 1)
# for _ in range(m):
#     a,b,c = map(int, input().split())
#     graph[a].append((b, c))
#     graph[b].append((a, c))

# q = []
# def dijkstra(start):
#     distance[start] = 0
#     heapq.heappush(q, (start, 0))
#     while q:
#         now, dist = heapq.heappop(q)
#         if distance[now] < dist:
#             continue
#         for i in graph[now]:
#             cost = dist + i[1]
#             if cost< distance[i[0]]:
#                 distance[i[0]] = cost
#                 heapq.heappush(q, (i[0], cost))

# dijkstra(start)

# for i in range(1, n + 1):
#     if distance[i] == INF:
#         print('inf')
#     else:
#         print(distance[i])

from 나동빈.알고리즘구현.서로소 import find_parent, union_parent

def find_parent(parent, x):
    if parent[x]!= x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]
    
def union_parent(parent, a, b):
    x = find_parent(parent, a)
    y = find_parent(parent, b)
    if x< y:
        parent[b] = a
    else:
        parent[a] = b

v, e = map(int, input().split())
parent = [0] * (v + 1)
for i in range(1, v+1):
    parent[i] = i

edges = []
for _ in range(e):
    a,b,c = map(int, input().split())
    edges.append((c, a, b))

edges.sort()
result = 0
for edge in edges:
    cost, a, b = edge
    if find_parent(parent, a)!= find_parent(parent, b):
        union_parent(parent, a, b)
        result += cost