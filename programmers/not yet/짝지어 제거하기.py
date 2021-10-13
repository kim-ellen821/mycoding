def shrink(s):
    for i in range(len(s)-1):
        if s[i] == s[i+1]:
            tmp = s[0:i] + s[i+2:]
            return tmp
    return s
        
            
def solution(s):
    while len(s)!=0:
        next = shrink(s)
        # print("줄:",end=' ')
        # print(next)
        if next == "":
            return 1
        elif s == next:
            return 0
        else:
            s = next
s = input()
ans = solution(s)
print(ans)