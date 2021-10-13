def solution(n, lost, reserve):
    
    for x in lost[:]:
        for y in reserve[:]:
            if x == y:
                lost.remove(x)
                reserve.remove(y)
                break

    for x in lost[:]:
        for y in reserve[:]:      
            if x - 1 == y or x + 1 == y:
                lost.remove(x)
                reserve.remove(y)
                break
                
    answer = n - len(lost)
    return answer
n = 5
lost = [1,2,3]
reserve = [2,3,4]
ans = solution(n, lost, reserve)
print(ans)
