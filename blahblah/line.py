# student, k, result = [0,1,0,0], 1, 6
# #student, k, result = [0, 1, 0, 0, 1, 1, 0], 2, 8
# #student, k, result = [0, 1, 0], 2, 0
# count = 0

# #start, end = 0, 0
# n = len(student)
# for i in range(n):
#     end = i
#     partial_cnt = 0
#     # end값을 가능한 만큼 증가시킨 다음
#     while partial_cnt <= k and end < n: # and student[end] != 1:
#         if student[end] == 1: partial_cnt += 1
#         if partial_cnt == k:
#             count += 1
#         end += 1
        
    
        
#     # start값을 1 증가시키기 전에 해당 수열의 값을 빼준다.
#     #partial_sum -= data[start]
# print(count)

research = ["abaaaa","aaa","abaaaaaa","fzfffffffa"]
n, k = 2, 2
#research = ["yxxy","xxyyy"]
#n, k = 2, 1
#research = ["yxxy","xxyyy","yz"]
#research = ["xy","xy"]
#n, k = 1, 1
from collections import Counter
answer =''
size = (len(research))
counter = [[] for _ in range(size)]
s_counter = [[] for _ in range(size)]

for i in range(size):
    counter[i] = dict(Counter(research[i]))
    s_counter[i] = sorted(counter[i].keys())
print(counter)
print(s_counter)

# for i in range(size - 1):
#     cnt = 0
#     for j in (s_counter[i]):
#         if j in counter[i+1]:
#             cnt += 1
#             if counter[i].get(j)>=k and counter[i+1].get(j)>=k and counter[i].get(j) + counter[i+1].get(j) >= 2* n* k:

tmp = []
for i in range(size - 1):
    for j in (s_counter[i]):
        tot = 0
        for day in range(n):          
            #if counter[i+day].get(j)>=k and counter[i+day].get(j)>=k and counter[i].get(j) + counter[i+1].get(j) >= 2* n* k:
            if j in counter[i+day] and counter[i+day].get(j)>=k:
                tot += counter[i+day].get(j)
        if tot>= 2*n*k:
            tmp.append(j)
print(tmp)
ans_counter = Counter(tmp)
print(ans_counter)
