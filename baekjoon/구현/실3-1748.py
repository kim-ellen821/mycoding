def find(n):
    digit = 1
    while 10 ** digit <= n:
        digit += 1
    return digit

n = int(input())
#현재 단어의 길이
num = find(n)
#print("자릿수:",num)
answer = 0
# 현재 단어 길이 이전자리까지 더해줌
# 9 * 자리수길이 * 10^n자리 더해줌
for i in range(num-1):
    answer += 9 * (i + 1) * (10 ** i)
#print("현재:", answer) 
#남은 번호에 대한 계산
left = n - 10 ** (num-1) + 1
#print("남은거:", left)
answer += num * left
print(answer)