test = "one4seveneight"

from collections import deque

num = ['0','1','2','3','4','5','6','7','8','9']

answer = []
s = deque(test)

while s:
    if s[0] in num:
        answer.append(s[0])
        s.popleft()
    elif s[0] == 'z':
        answer.append('0')
        for _ in range(4):
            s.popleft()
    elif s[0] == 'o':
        answer.append('1')
        for _ in range(3):
            s.popleft()
    elif s[0] == 't':
        if s[1] == 'w':
            answer.append('2')
            for _ in range(3):
                s.popleft()
        elif s[1] =='h':
            answer.append('3')
            for _ in range(5):
                s.popleft()
    elif s[0] =='f':
        if s[1] == 'o':
            answer.append('4')
        elif s[1] == 'i':
            answer.append('5')
        for _ in range(4):
                s.popleft()
    elif s[0] =='s':
        if s[1] == 'i':
            answer.append('6')
            for _ in range(3):
                s.popleft()
        elif s[1] == 'e':
            answer.append('7')
        for _ in range(5):
                s.popleft()
    elif s[0] == 'e':
        answer.append('8')
        for _ in range(5):
            s.popleft()
    else:
        answer.append('9')
        for _ in range(4):
            s.popleft()
ans =''
for i in answer:
    ans += i

fin = int(ans)       
print(ans)


#print(ord('a'), ord('z'))