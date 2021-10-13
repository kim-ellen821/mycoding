# import sys
# sys.setrecursionlimit(10000)

# n = int(input())
# INF = int(1e9)
# d = [INF] * (n + 1)


# def find(n):
#     if d[n]!=INF:
#         return d[n]
#     else:
#         if n == 1:
#             d[n] = 0
#             return 0
#         elif n == 2:
#             d[n] = 1
#             return 1
#         else:
#             d[n] = find(n-1) + 1
#             if n % 3 == 0:
#                 d[n] = min(d[n], find(n//3) + 1)
#             elif n % 2 == 0:
#                 d[n] = min(d[n], find(n//2) + 1)
#     return d[n]
# ans = find(n)
# print(d[n])

n = int(input())

d = [0] * (int(10e6) + 1)

for i in range(2, n+1):
    d[i] = d[i-1] + 1
    if i % 2 == 0:
        d[i] = min(d[i], d[i//2] + 1)
    if i % 3 == 0:
        d[i] = min(d[i], d[i//3] + 1)
print(d[n])