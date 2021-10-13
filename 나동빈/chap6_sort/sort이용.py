# def solution(array, commands):
#     temp =[]
#     ans = []
#     size=len(commands)
#     for i in range(size):
#         start= int(commands[i][0] - 1)
#         end = int(commands[i][1])
#         want = int(commands[i][2] - 1)
#         temp = array[start:end]
#         ans.append(temp[want])
#     return ans

# def coinChange(coins, amount):
#     coins.sort(reverse=True)

#     length = len(coins)
#     count = 0
#     if amount == 0:
#         return count
#     else:
#         for i in range(length):
#             if amount ==0: return count
#             if amount // coins[i] >= 1:
#                 temp = amount//coins[i]
#                 amount %= coins[i]
#                 count += temp
#             elif amount//coins[i]<1:
#                 continue
#     return -1

# coins=[1,2,5]
# amount =11
# ans = coinChange(coins, amount)      
# print(ans)

#n, target = list(map(int, input().split()))

array = [('바나나', 2), ('사과', 5), ('당근', 3)]

def setting(data):
    return data[1]

result = sorted(array)#, key= setting)
print(result)