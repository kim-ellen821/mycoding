n = int(input())
numbers = [int(input()) for _ in range(n)]
big = max(numbers)
count = [0] * (big + 1)
count[1], count[2], count[3] = 1, 2, 4

for i in range(4, max(numbers) + 1):
    count[i] = (count[i-1] + count[i-2] + count[i-3]) % 1000000009
for num in numbers:
    print(count[num])