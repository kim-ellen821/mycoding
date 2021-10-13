from itertools import combinations
import math

n, s = map(int, input().split())
kids = list(map(int, input().split()))
distance = []
for kid in kids:
    tmp = abs(s - kid)
    if len(distance) == 0:
        distance.append(tmp)
    else:
        now = distance.pop()
        next = math.gcd(now, tmp)
        distance.append(next)
#     for i in distance:
#         if tmp in distance or tmp % i == 0:
#             continue
#         else:
#             distance.append(tmp)
# print(distance)

# d = int(1e9)
# all = list(combinations(distance,2))
# for i in all:
#     tmp = math.gcd(i[0], i[1])
#     if d > tmp:
#         d = tmp
# print(d)
print(distance[0])