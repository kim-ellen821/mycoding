from itertools import combinations

N, M = map(int, input().split())
numbers = list(combinations(range(1, N+1), M))
for num in numbers:
    print(' '.join(map(str, num)))