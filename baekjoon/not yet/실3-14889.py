from itertools import combinations
answer = int(1e9)
n = int(input())
all = [i for i in range(n)]
team = [list(map(int, input().split())) for _ in range(n)]
possible = list(combinations(all, n//2))

for i in range(len(possible)//2):
    A = set(possible[i])
    B = set(all) - A
    a = list(combinations(A,2))
    asum = 0
    for x, y in a:
        asum += team[x][y] + team[y][x]
    b = list(combinations(B,2))
    bsum = 0
    for x, y in b:
        bsum += team[x][y] + team[y][x]
    if answer> abs(asum - bsum):
        answer = abs(asum - bsum)

print(answer)
# for A in possible:
#     B = []
#     for i in range(n):
#         if i not in A: B.append(i)
#     print(A, B)
#     a = list(combinations(A,2))
#     b = list(combinations(B,2))
#     #print(a[0][0], a[0][1])
#     print(a, b)
#     for i in range(len(a)):
#         print(team[a[i][0]][a[i][1]], team[a[i][1]][a[i][0]], team[b[i][0]][b[i][1]], team[b[i][1]][b[i][0]])
#         tmp = abs(team[a[i][0]][a[i][1]] + team[a[i][1]][a[i][0]]- team[b[i][0]][b[i][1]] - team[b[i][1]][b[i][0]])
#     if tmp<answer:
#         answer = tmp
# print(answer)