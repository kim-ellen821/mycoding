# k, n = map(int, input().split())
# arr = []
# for _ in range(k):
#     arr.append(int(input()))

# def count(n, arr):
#     start = 1
#     end = min(arr)
#     sizes = []
#     while start <= end:
#         size = (start + end) // 2
#         count = 0
#         print(start, size, end)
#         for x in arr:
#             count += (x // size)
#         print(count)
#         if count == n:
#              sizes.append(size)
#         if count < n:
#             end = size - 1
#         else:
#             start = size + 1
#             sizes.append(size)
#     return max(sizes)

# ans = count(n, arr)
# print(ans)

k, n = map(int, input().split())
arr = []
for _ in range(k):
    arr.append(int(input()))

def count(n, arr):
    start = 1
    end = max(arr)
    sizes = []
    while start <= end:
        size = (start + end) // 2
        count = 0
        for x in arr:
            count += (x // size)
        if count == n:
             sizes.append(size)
        if count < n:
            end = size - 1
        else:
            start = size + 1
            sizes.append(size)
    return max(sizes)

ans = count(n, arr)
print(ans)