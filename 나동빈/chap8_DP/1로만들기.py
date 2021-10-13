###global로 설정해둔 변수는 
# 함수내에서 조작 불가능하므로
#값을 받고 싶은거라면 return으로 해주지
#d[i]=어떤 값 으로 하지 않도록 주의~

d = [0] * 100

def find(n):
    if n == 1:
        return 0
    elif n == 2 :
        return 1
     
    if d[n] != 0:
        return d[n]
    d[n] = find(n - 1) + 1
    if n % 5 == 0:
        d[n] = min(d[n], find(n//5) + 1)
    elif n % 3 == 0:
        d[n] = min(d[n], find(n//3) + 1)
    elif n % 2 == 0:
        d[n] = min(d[n], find(n//2) + 1)
    return d[n]

n = int(input())
ans = find(n)
print(ans)