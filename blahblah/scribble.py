# #2
# h ,w = 4, 4
# blocks = [[0,0], [3,1], [1,0], [0,0], [2,2], [2,3], [3,1]]
# map = [0] * 100001

# answer = []
# def solution(h, w, blocks):
#     check = dict()
#     for i in range(len(blocks)):
#         s = str(blocks[i][0]) + str(blocks[i][1])
#         print(s)
#         if s not in check:
#             map[blocks[i][1]] += 1
#             check[s] = True
#     answer.append(w-map[0])
#     for i in range(1, h):
#         answer.append(w-map[i] + answer[i-1])
#     print(answer)

# solution(h, w, blocks)

#1316

#print(ord('a'), ord('z'))
# MAX = int(1e9)
# coins = list(map(int, input().split()))
# amount = int(input())
# dp = [MAX] * (amount + 1)
# dp[0] = 0
# for coin in coins:
#     for i in range(coin, amount + 1):
#         dp[i] = min(dp[i], dp[i-coin]+1)
# if dp[amount]==MAX:
#     print(-1)
# else:
#     print(dp[amount])

N, A = map(int, input().split())
val = ""
for i in range(A) :
    C, K = input().split()
    K = int(K)
    val += C * K

for i in range(len(val)) :
    if (i + 1) % N == 0 :
        print(val[i])
    else :
        print(val[i], end="")
print()