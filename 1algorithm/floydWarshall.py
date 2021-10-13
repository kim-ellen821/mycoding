INF = int(1e9)

#노드의 개수 및 간선의 개수를 입력받기
n = int(input())
m = int(input())
#2차원 리스트(그래프 표현)를 만들고, 모든 값을 무한으로 초기화
graph = [[INF]* (n + 1) for _ in range(n + 1)]
#본인->본인 노드로 가는 것의 비용 0으로 초기화
for i in range(1, n+1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

#각 간선에 대한 정보를 입력받아, 그 값으로 초기화
for _ in range(m):
    #A->B로 가는 비용:C
    a,b,c = map(int, input().split())
    graph[a][b] = c

#점화식에 따라 플로이드 워셜 알고리즘을 수행
for i in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][i] + graph[i][b])

for i in range(1, n + 1):
    for j in range(1, n + 1):
        #도달할 수 없는 경우 infinity라고 출력
        if graph[i][j] == INF:
            print("infinity", end = ' ')
        else:
            print(graph[a][b], end=' ')
    print()