import math
n = int(input())

for _ in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    
    dist = math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)
    if dist == 0 and r1 == r2:
        print(-1)
    else:
        r = r1 + r2
        if dist == r or dist == abs(r1 - r2):
            print(1)
        elif dist < r:
            if dist < abs(r1 - r2):
                print(0)
            else:
                print(2)
        else:
            print(0)