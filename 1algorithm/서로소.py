def find_parent(parent, x):
    if parent[x]!=x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드와 간선개수 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1)

#부모 테이블상에서, 부모를 자기 자신으로 초기화
for i in range(1, v + 1):
    parent[i] = i



#################집합 확인#######################
# #union연산
# for i in range(e):
#     a, b = map(int, input().split())
#     union_parent(parent, a, b)

# print('각 원소가 속한 집합:', end='')
# for i in range(1, v + 1):
#     print(find_parent(parent, i), end=' ')

# print()

# print('부모 테이블: ',end='')
# for i in range(1, v + 1):
#     print(parent[i], end = ' ')

#################사이클 판별######################
###무향 그래프에만 적용 가능!!################
cycle = False
for i in range(e):
    a, b =map(int, input().split())
    #사이클이 발생한 경우 종료
    if find_parent(parent, a) == find_parent(parent, b):
        cycle = True
        break
    else:
        union_parent(parent, a, b)

if cycle:
    print("cycle 발생")
else:
    print("no cycle!")