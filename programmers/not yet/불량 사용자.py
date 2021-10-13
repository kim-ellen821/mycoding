#user_id , banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "abc1**"]
#user_id , banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"],	["*rodo", "*rodo", "******"]
user_id , banned_id = ["frodo", "fradi", "crodo", "abc123", "frodoc"],	["fr*d*", "*rodo", "******", "******"]
from itertools import permutations

def check(tmp, banned_id):
    #print(tmp, banned_id)
    for i in range(len(banned_id)):
        #print('비교:',end=' ')
        #print(tmp[i], banned_id[i])
        if len(tmp[i])!= len(banned_id[i]):
            #print('길이 다름')
            return False
        else:
            for k in range(len(banned_id[i])):
                if banned_id[i][k]!='*' and banned_id[i][k] != tmp[i][k]:
                    #print('문자 다름')
                    #print(banned_id[i][k], user_id[i][k])
                    return False
    #print('가능')
    return True
    
def solution(user_id, banned_id):
    answer = []
    # can = [[]for _ in range(len(banned_id))]
    # count = -1
    # for i in range(len(banned_id)):
    #     count+=1
    #     for j in range(len(user_id)):
    #         check = True
    #         if len(banned_id[i]) != len(user_id[j]):
    #             check = False
    #             continue
    #         elif len(banned_id[i]) == len(user_id[j]):
    #             for k in range(len(banned_id[i])):
    #                 if banned_id[i][k]!='*' and banned_id[i][k] != user_id[j][k]:
    #                     check = False
    #                     break  
    #         if check:
    #             can[count].append(user_id[j])
    # #print(can)
    can = list(permutations(user_id, len(banned_id)))
    for tmp in can:
        #print(tmp, end='띄어 ')
        if check(tmp, banned_id):
            print("가능:",end=' ')
            print(tmp, banned_id)
            tmp = set(tmp)
            if tmp not in answer:
                answer.append(tmp)
    #print(answer)
    #print(check(can[7], banned_id))
    #print()    

    return len(answer)
solution(user_id, banned_id)