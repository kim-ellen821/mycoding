# from collections import deque
# n = int(input())
# arr = list(map(int, input().split()))
# dp = arr[:]
# for i in range(1, n):
#     for j in range(i):
#         if arr[j]< arr[i]:
#             dp[i] = max(dp[i], dp[j]+ arr[i])
# for i in range(n):
#     tmp = 0
#     q = deque()
#     for j in range(i):
#         if arr[j] < arr[i]:
#             if len(q) == 0:
#                 q.append(arr[j])
#             else:
#                 small = q.pop()
#                 if small< arr[j]:
#                     q.append(small)
#                     q.append(arr[j])
#         tmp = sum(q) + arr[i]
#     if max<tmp:
#         max = tmp
#     print(i, tmp, max)
# print(max)
# print(max(dp))

n = int(input())
arr = list(map(int, input().split()))
val = arr[:]
for i in range(n):
    for j in range(i):
        if arr[j]< arr[i]:
            val[i] = max(arr[i] + val[j], val[i])
print(max(val))