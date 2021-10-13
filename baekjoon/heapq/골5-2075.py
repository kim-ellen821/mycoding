# import heapq

# n = int(input())

# board = [[] for _ in range(n)]
# for i in range(n):
#     board[i] = list(map(int, input().split()))

# arr = []
# turn = []
# for i in range(n):
#     arr.append((board[n-1][i], i))
# arr.sort(reverse = True)
# for i in range(n):
#     turn.append(arr[i][1])
# print(turn)

# count = [1] * (n)

# q = []
# for i in range(n):
#     heapq.heappush(q, (-board[n-1][i], (board[n-1][i], turn[i])))

# for _ in range(n):
#     x = heapq.heappop(q)
#     tmp = x[1][0]
#     count[tmp] += 1
    
#     heapq.heappush(q, (-board[n- count[tmp]]))

import heapq

q = []
n = int(input())

board = [[] for _ in range(n)]
for i in range(n):
    arr = list(map(int, input().split()))
    if len(q) == 0:
        for j in arr:
            heapq.heappush(q, j)
    else:
        for j in range(n):
            heapq.heappush(q, arr[j])
            heapq.heappop(q)

print(q[0])


