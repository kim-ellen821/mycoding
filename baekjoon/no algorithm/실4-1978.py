import math

primenum = [True] * 1001
primenum[0] = False
primenum[1] = False
for i in range(2, int(math.sqrt(1001))):
    if primenum[i] == True:
        j = 2
        while i * j <= 1000:
            primenum[i * j] = False
            j += 1

n = int(input())
ans = 0
check = list(map(int, input().split()))
for i in range(n):
    if primenum[check[i]] == True:
        ans += 1
print(ans)