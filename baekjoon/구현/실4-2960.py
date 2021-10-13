# n, k = map(int, input().split())
# arr = [True] * (n + 1)
# count = 0
# for i in range(2, n + 1):
#     for j in range(i, n+1, i):
#         arr[i * j] = False
#         count += 1
#         j += 1

# visit = [False] * (n + 1)
# count = 0
# # for i in range(2, n+1):
# #     if arr[i] and not visit[i]:
# #         j = 1
# #         while i * j <= n:
# #             if count == k:
# #                 print(i * j)
# #                 break
# #             else:
# #                 visit[i * j] = True
# #                 count += 1
# #                 j += 1
# i , j = 2, 1
# if arr[i] and not visit[i]:
#     while i * j <= n:
#         if count == k:
#             print(i * j)
#         else:
#             visit[i * j] = True
#             count += 1
#             j += 1
#     i += 1

n, k = map(int, input().split())
visit = [False] * (n + 1)
count = 0
for i in range(2, n + 1):
    for j in range(i, n+1, i):
        if not visit[j]:
            visit[j] = True
            count += 1
            if count == k:
                print(j)
                break