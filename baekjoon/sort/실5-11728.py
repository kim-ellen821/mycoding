
N, M  = map(int, input().split())
tot = set()
A = list(map(int, input().split()))
B = list(map(int, input().split()))
tot = A+B
tot.sort()
for i in range(len(tot)):
    print(tot[i], end=' ')