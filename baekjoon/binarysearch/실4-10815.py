import sys
input = sys.stdin.readline

def find(target):
    start = 0
    end = N-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return 1
        elif arr[mid]<target:
            start = mid + 1
        elif arr[mid]>target:
            end = mid - 1
    return 0

N = int(input())
arr = list(map(int, input().split()))
arr.sort()
M = int(input())
for num in list(map(int, input().split())):
    print(find(num), end=' ')
# check = list(map(int, input().split()))
# answer = []

# for i in range(len(check)):
#     if find(0, N-1, check[i], have):
#         answer.append(1)
#     else:
#         answer.append(0)
# for i in answer:
#     print(i, end=' ')