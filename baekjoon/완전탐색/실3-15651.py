from itertools import product
n, m = map(int, input().split())
numbers = list(product(range(1, n+1), repeat = m))
for num in numbers:
    print(' '.join(map(str, num)))