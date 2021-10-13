from itertools import combinations
import math

n = int(input())

for _ in range(n):
    answer = 0
    test = list(map(int, input().split()))
    com = list(combinations(test[1:len(test)], 2))
    for i in range(len(com)):
        answer += (math.gcd(com[i][0], com[i][1]))
    print(answer)