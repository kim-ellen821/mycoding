import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.insert(0, 0)

for i in range(1, N + 1):
    arr[i] += arr[i-1]
for _ in range(M):
    i, j = map(int, input().split())
    ans = arr[j] - arr[i - 1]
    print(ans)

# N, M = map(int, input().split())
# arr = list(map(int, input().split()))
# for _ in range(M):
#     a, b= map(int, input().split())
#     tmp = 0
#     for i in range(a - 1, b):
#         tmp += arr[i]
#     print(tmp)