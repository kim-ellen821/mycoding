import math
import sys
input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]
num = (max(numbers))
isprime = [True] * (num + 1)
isprime[1] = False

for i in range(2, int(math.sqrt(num)) + 1):
    j = 2
    while i*j <= num:
        isprime[i*j] = False
        j += 1

for num in numbers:
    ans = 0
    for i in range(2, num//2 + 1):
        if isprime[i] and isprime[num - i]:
            ans += 1
    print(ans)

# for _ in range(n):
#     x = int(input())
#     count = 0
#     for i in range(2, x//2 + 1):
#         if arr[i] == True and arr[x - i] == True:
#             count += 1
#     print(count)