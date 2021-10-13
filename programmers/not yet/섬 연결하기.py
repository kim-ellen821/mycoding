n = 4
costs = [[0,1,1],[0,2,2],[1,2,5],[1,3,1],[2,3,8]]

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a< b:
        parent[b] = a
    else:
        parent[a] = b
        
def solution(n, costs):
    answer = 0
    size = len(costs)
    graph = [[] for _ in range(size)]    
    parent = [0] * (n+1)
    for i in range(1, n+1):
        parent[i] = i
        
    edges = []
    
    for i in range(size):
        edges.append((costs[i][2], costs[i][0], costs[i][1]))

    edges.sort()

    for edge in edges:
        cost, a, b = edge
        if find_parent(parent, a) != find_parent(parent, b):
            union_parent(parent, a, b)
            answer += cost

    return answer

ans = solution(n, costs)
print(ans)