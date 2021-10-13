import math

x = int(input())
y = int(input())

nums = [True] * (y + 1)

for i in range(2, int(math.sqrt(y)) + 1):
    if nums[i] == True:
        j = 2
        while i * j <= y:
            nums[i*j] = False
            j += 1
primeNum = []
for i in range(x, y + 1):
    if i == 1:
        continue
    if nums[i]:
        primeNum.append(i)
if len(primeNum) == 0:
    print(-1)
else:
    print(sum(primeNum))
    print(min(primeNum))