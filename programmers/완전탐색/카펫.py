brown, yellow = map(int, input().split())

answer = []
#print(1//2 + 1)
if yellow == 1:
    answer.append(3)
    answer.append(3)
else:
    for i in range(1, (yellow // 2) + 1):
        if yellow % i == 0:
            a = i
            b = yellow // i
            if a * 2 + b * 2 + 4 == brown:
                answer.append(b + 2)
                answer.append(a + 2)
                break
print(answer)
