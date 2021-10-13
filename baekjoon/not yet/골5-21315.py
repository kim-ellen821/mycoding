from collections import deque

n = int(input())
fin = list(map(int, input().split()))

def card(k, arr):
    for _ in range(2 ** k):
        x = arr.pop()
        arr.appendleft(x)
    for i in range(2, k + 2):
        j = 2 ** (k - i + 1)
        move = list(arr[i : i+j])
        print(move)       

arr = deque(i for i in range(1, n + 1))

# for i in range(1, 9):
#     for j in range(1, 9):
#         tmp = card(i, arr)
#         tmp2 = card(j, tmp)
#         if tmp2 == fin:
#             print(i, j)
#             break

card(2, arr)
