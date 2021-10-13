import math
w , h = 8, 12

def solution(w,h):
    tot = w * h
    num = math.gcd(w, h)
    
    x = w // num
    y = h // num
    long = max(x, y)
    print(long)
    if long == 1:
        square = 1
    elif long == 2:
        square = 2
    elif long == 3:
        square = 4
    else:
        square = 2 + 4 * ((y//2) - 1)
        print(square)
        if y % 2 == 1:
            square += 1
        print(square)
    s_tot = square * num
    print(s_tot)        
        
    answer = tot - s_tot
    return answer

ans  = solution(w, h)
print(ans)