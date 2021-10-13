#print(-3//-2)
Num = int(input())
ans = ''
if Num == 0:
    print(0)
    exit()
while Num:
    if Num % -2 == 0:
        print(Num, end=' ')
        Num = Num//-2
        ans = '0' + ans
        print(Num)
    else:
        print(Num, end=' ')
        Num = Num//-2 + 1
        ans = '1' + ans
        print(Num)
print(ans)