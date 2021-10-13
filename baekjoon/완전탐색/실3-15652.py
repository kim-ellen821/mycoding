from itertools import combinations_with_replacement
n, m = map(int, input().split())
numbers = list(combinations_with_replacement(range(1, n+1), m))
for num in numbers:
    print(' '.join(map(str, num)))