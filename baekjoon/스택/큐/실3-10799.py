#######시간 초과######
# import sys
# from collections import deque

# input = sys.stdin.readline

# l = input().rstrip()

# all = deque()
# lasers = []
# sticks = []

# for i in range(len(l)):
#     if l[i]=='(':
#         all.append((i))
#     else:
#         left = all.pop()
#         if i-left == 1: lasers.append(i)
#         else: sticks.append((left, i))

# tot = len(sticks)
# for laser in lasers:
#     for stick in sticks:
#        if stick[0]<laser<stick[1]:
#            tot += 1
# print(tot) 

import sys

input = sys.stdin.readline

arr = input().rstrip()
left = 0
tot = 0
for i in range(len(arr)):
    if arr[i] =='(':
        left += 1
    else:
        left -= 1
        if arr[i-1] =='(':
            tot += left
        else:
            tot += 1
print(tot)