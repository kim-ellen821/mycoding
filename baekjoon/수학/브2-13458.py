N = int(input())
A = list(map(int, input().split()))
B, C = map(int, input().split())
ans = len(A)
for num in A:
    tmp = num
    tmp -= B
    if tmp>0:
        if tmp % C == 0: ans += tmp//C
        else: ans += tmp//C + 1
print(ans)