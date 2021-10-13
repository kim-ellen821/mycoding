s1 = "{{2},{2,1},{2,1,3},{2,1,3,4}}"
s2 = "{{1,2,3},{2,1},{1,2,4,3},{2}}"
s3 = "{{20,111},{111}}"
s4 = "{{123}}"
s5 = "{{4,2,3},{3},{2,3,4,1},{2,3}}"

num = "0123456789"
# def solution(s):
#     count = 0
#     size = -1
#     for i in s:
#         if i == '}':
#             size += 1
#     arr = [[] for _ in range(size)]
#     tmp=''   
#     for i in range(2, len(s)):
#         if s[i]=='{':
#             count += 1
#         elif s[i] in num:
#             tmp += s[i]
#             if s[i+1] =='}'or s[i+1]==',':
#                 arr[count].append(int(tmp))
#                 tmp=''
#     arr.sort(key = lambda x: len(x))
#     answer = []
#     answer.append(arr[0][0])
    
#     for i in range(1, size):
#         for j in arr[i]:
#             if j not in answer:
#                 answer.append(j)
#     return answer
import re
def solution(s):
    answer = []
    a = s.split(',{')
    s = s.split('},')
    # print(a)
    # print(s)
    s.sort(key = lambda x: len(x))
    print(s)
    for word in s:
        numbers = re.findall("\d+", word)
        for num in numbers:
            if int(num) not in answer:
                answer.append(int(num))
    return answer
ans = solution(s2)
print(ans)