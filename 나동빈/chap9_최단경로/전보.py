import heapq

INF = int(1e9)

n, m, start = map(int, input().split())
distance = [INF] * (n + 1)
graph = [[]for _ in range(n + 1)]
for _ in range(m):
    a,b,c = map(int, input().split())
    graph[a].append((b, c))

def dijkstra(start):
    q = []
    distance[start] = 0
    heapq.heappush(q, (start, 0))
    while q:
        now, dist = heapq.heappop(q)
        if distance[now] < dist:
            continue
        for i in graph[now]:
            cost = dist + i[1]
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (i[0], cost))

dijkstra(start)
ans = []
path = []
tot = 0
for i in range(2, n+1):
    if distance[i] != INF:
        tot += 1
        path.append(distance[i])
ans.append(tot)
ans.append(max(path))
print(ans)