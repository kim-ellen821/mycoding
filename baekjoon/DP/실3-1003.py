arr = [[0] * 2 for _ in range(41)]
#arr[0][0], arr[0][1] = 1, 0
#arr[1][0], arr[1][1] = 0, 1

def fibo(num):
    if num == 0:
        return [1, 0]
    elif num == 1:
        return [0, 1]

    elif arr[num][0]!= 0 or arr[num][1]!=0:
        return arr[num]
    else:
        arr[num][0] = fibo(num-1)[0] + fibo(num - 2)[0]
        arr[num][1] = fibo(num-1)[1] + fibo(num - 2)[1]
        return arr[num]


k = int(input())
for _ in range(k):
    num = int(input())
    ans = fibo(num)
    print(ans[0], ans[1])