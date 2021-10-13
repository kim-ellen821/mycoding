# from itertools import permutations
# import math

# def nCr(n,r):
#     return int(math.factorial(n)/(math.factorial(r) * math.factorial(n-r)))

# n, m = map(int, input().split())
# num = list(map(int, input().split()))
# other =[]
# for i in range(10):
#     if i not in num: other.append(i)

# #for i in range(len(num), n+1):
# print(nCr(2, 2), nCr(2,1))   

import math

def nCr(n,r):
    return int(math.factorial(n)/(math.factorial(r) * math.factorial(n-r)))
n, m = map(int, input().split())
num = list(map(int, input().split()))
answer = 0
count = 10
for i in range(m+1):
    answer += (pow(-1, i))*pow(count, n)*nCr(m,i)
    count -=1
print(answer)