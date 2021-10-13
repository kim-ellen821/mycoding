#answers=[1,2,3,4,5]
answers =[1,3,2,4,2]
s1 = [1, 2, 3, 4, 5]
s2 = [2, 1, 2, 3, 2, 4, 2, 5]
s3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]

answer =[]

size = len(answers)
c1, c2, c3 = 0, 0, 0
for i in range(size):
    if answers[i] == s1[i % 5]:
        c1 += 1
    if answers[i] == s2[i % 8]:
        c2 += 1
    if answers[i] == s3[i % 10]:
        c3 += 1
most = max(c1, c2, c3)
if most == c1:
    answer.append(1)
if most == c2:
    answer.append(2)
if most == c3:
    answer.append(3)
print(answer)