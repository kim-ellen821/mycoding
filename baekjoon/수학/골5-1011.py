import math
N = int(input())
for _ in range(N):
    x, y = map(int,input().split())
    ans = 0
    dist = math.sqrt(y-x)
    num = math.floor(dist)
    if dist-num == 0: ans = num * 2 - 1
    else:
        if dist - num <0.5: ans = num * 2
        elif dist - num >= 0.5: ans = num * 2 + 1
    print(ans)