#1
#문제: 1~10 사이에 있는 소수를 출력하시오
prime_list = []

for num in range(2, 11):
    is_prime = True
    for j in range(2, num):
        if num % j == 0:
            is_prime = False
    if is_prime:
        prime_list.append(num)

print(prime_list)


# #질문
# 1. 일단 for문 들어갔다가 반복하고 나오고 이러한 과정이 저기서 존나 헷갈림
# 2. is_prime = True 라는 문이 첫번째 for문안에 들어가지 않고 밖에 먼저 있으면 결과가 달라지는데 무슨 차이인지 모르겠음


# #질문 2에 대한 코드
# print()
# print()


# prime_list = []
# is_prime = True
# for num in range(2, 11):
#     for j in range(2, num):
#         if num % j == 0:
#             is_prime = False
#     if is_prime:
#         prime_list.append(num)

# print(prime_list)