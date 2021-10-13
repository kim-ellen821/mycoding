count = int(input())
tot = [0] * 12
tot[1], tot[2], tot[3] = 1, 2, 4
def find(num):
    if tot[num] == 0:
        tmp = 0
        for i in range(1, 4):
            tmp += find(num - i)
        return tmp
    return tot[num]
for _ in range(count):
    num = int(input())
    ans = find(num)
    print(ans)