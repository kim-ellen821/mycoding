#people = [70, 50, 80, 50]
#limit = 100

people = [70, 80, 50]
limit = 100

# def solution(people, limit):
#     answer = 0
#     arr = [False] * (len(people))
#     for i in range(len(people)):
#         if not arr[i]:
#             arr[i] = True
#             left = limit - people[i]
#             for j in range(i, len(people)):
#                 #무게최대값,index 쌍
#                 temp = (0, 0)
#                 if not arr[j] and people[j] <= left:
#                     if temp[0] < people[j]:
#                         temp = (people[j], j)
#             if temp[0]!= 0:
#                 arr[temp[1]]=True
#             answer += 1
#     return answer

# ans = solution(people, limit)
# print(ans)


# def solution(people, limit):
#     answer = 0
#     arr = [False] * (len(people))
#     people.sort()
    
#     for i in range(len(people)):
#         if not arr[i]:
#             arr[i] = True
#             if people[i] <= (limit) //2:
#                 for j in range(len(people) - 1, i , -1):
#                     if not arr[j]:
#                         arr[j] = True
#                         break
#             else:
#                 for j in range(len(people) - 1, i , -1):
#                     if not arr[j] and people[j] <= limit - people[i]:
#                         arr[j] = True
#                         break
#             answer += 1
#     return answer

from collections import deque

def solution(people, limit):
    answer = 0
    people.sort()
    p = deque(people)
    print(p)
    while p:
        x = p.pop()
        if x <= limit//2:
            if len(p) != 0:
                p.popleft()
        else:
            if len(p) != 0:
                y = p.popleft()
                if x + y > limit:
                    p.appendleft(y)
        answer += 1
    return answer

ans = solution(people, limit)
print(ans)