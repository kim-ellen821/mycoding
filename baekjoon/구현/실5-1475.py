import math
n = input()
n = [int(x) for x in n]
count = [0] * 10

for i in n:
    count[i] += 1
count[6] = math.ceil((count[6] + count[9])/2)
count[9] = 0
ans = max(count)
print(ans)