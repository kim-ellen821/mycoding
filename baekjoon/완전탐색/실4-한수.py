def find(n):
    ans = 0
    size = len(str(n))
    if size == 1 or size == 2:
        ans = n
    elif size == 3:
        ans = 99
        for i in range(100, n + 1):
            num = str(i)
            if int(num[0])- int(num[1]) == int(num[1]) - int(num[2]):
                ans += 1
    else:
        return find(999)
    return ans

n = int(input())
answer = find(n)

print(answer)