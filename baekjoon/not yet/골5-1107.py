N = input()
M = int(input())
broke = list(map(int, input().split()))
answer = 0
def find(num, broke):
    can = []
    small = 11
    for i in range(10):
        if i not in broke:
            if abs(i-num)<small:
                if len(can)>0:
                    can.clear()
                else:
                    can.append(i)
                small = abs(i-num)
            elif abs(i-num) == small:
                can.append(i)


if N == 100:
    answer = 0
else:
    now=''
    for num in N:
        now += str(find(int(num), broke))
print(answer)