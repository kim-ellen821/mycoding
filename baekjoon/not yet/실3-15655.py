from itertools import combinations
n, m = map(int, input().split())
can = list(map(int, input().split()))
can.sort()
numbers = list(combinations(can, m))
for num in numbers:
    print(' '.join(map(str, num)))