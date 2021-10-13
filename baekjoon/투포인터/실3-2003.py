n, m = map(int, input().split())
arr = list(map(int, input().split()))
start, end = 0, 0

sum = 0
count = 0
# while end != n and start<=end:
#     sum += arr[end]
#     print('start, end, sum:', end='')
#     print(start, end, sum)
#     if sum >= m:
#         if sum == m:
#             count += 1
#         print('start, end, sum, count:', end='')
#         print(start, end, sum, count)
#         sum -= arr[start]
#         start += 1              
#     end += 1
for start in range(n):
    while end!=n and sum<m:
        sum += arr[end]
        end += 1
    if sum == m:
        count += 1
    sum -= arr[start]
print(count)