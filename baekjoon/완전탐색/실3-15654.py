from itertools import permutations
n, m = map(int, input().split())
can = list(map(int, input().split()))
can.sort()
numbers = list(permutations(can, m))
for num in numbers:
    print(' '.join(map(str, num)))
#print(' '.join(combinations(n, m)))
