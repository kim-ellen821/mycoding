from itertools import permutations
N, M = map(int, input().split())
numbers = list(i for i in range(1, N+1))
can = list(permutations(numbers, M))
for i in can:
    for j in range(len(i)):
        print(i[j], end=' ')
    print()