from itertools import permutations
import math

#numbers = "17"
numbers = "011"

arr = []

def make(big):
    global arr
    arr = [True] * (big + 1)
    arr[1] = False
    for i in range(2, int(math.sqrt(big)) + 1):
        j = 2
        while i * j <= big:
            arr[i * j] = False
            j += 1
    # for i in range(1, big + 1):
    #     if arr[i]:
    #         print(i, end=' ')

def solution(numbers):
    answer = 0
    # num = []
    # for x in numbers:
    #     num.append(int(x))
    num = list(numbers)
    # print(num)
    made = set()
    
    for i in range(1, len(num) + 1):
        #made |= set(map(int, map(''.join, permutations(num, i))))
        made.update(list(map(int, map(''.join, permutations(num, i)))))

        made |= set(map(int, map(''.join, permutations(num, i))))

    make(max(made))
    for i in made:
        if i == 0: continue
        #print(i, end=' ')
        if arr[i]:
            print('prime:',end='')
            print(i)
            answer += 1
    print(answer)
    return answer

solution(numbers)