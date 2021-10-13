N = int(input())

zoo = [[0] * 3 for _ in range(N)]

for i in range(3):
    zoo[0][i] = 1

for i in range(1, N):
    zoo[i][0] = (zoo[i-1][0] + zoo[i-1][1] + zoo[i-1][2]) %9901
    zoo[i][1] = (zoo[i-1][0] + zoo[i-1][2]) % 9901
    zoo[i][2] = (zoo[i-1][0] + zoo[i-1][1]) % 9901
print(sum(zoo[N-1])%9901) 