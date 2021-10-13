answer = 0
numbers = [1,1,1,1,1]

def dfs(numbers, target, now, count):
    if count == len(numbers) - 1:
        global answer
        if target == now - numbers[count]:
            answer += 1
        elif target == now + numbers[count]:
            answer += 1
    dfs(numbers, target, now + numbers[count], count+1)
    dfs(numbers, target, now - numbers[count], count+1)
    
def solution(numbers, target):
    dfs(numbers, target, 0, 0)
    return answer

solution(numbers, 3)