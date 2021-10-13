n = int(input())

for _ in range(n):
    a, b = map(int, input().split())
    x = max(a, b)
    y = min(a, b)
    while y:
        temp = x % y
        x = y
        y = temp
    GCD = x
    LCM = a * b // GCD

    print(LCM)