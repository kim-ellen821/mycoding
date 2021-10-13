n = int(input())

for _ in range(n):
    count = int(input())
    stick = [[] for _ in range(2)]
    val = [[0] * 100001 for _ in range(2)]
    for i in range(2):
        stick[i] = list(map(int, input().split()))
    
    for i in range(2):
        val[i][0] = stick[i][0]
    val[0][1] = stick[1][0] + stick[0][1]
    val[1][1] = stick[1][1] + stick[0][0]
    
    for i in range(2, count):
        val[0][i] = stick[0][i] + max(val[1][i-1], val[0][i-2], val[1][i-2])
        val[1][i] = stick[1][i] + max(val[0][i-1], val[0][i-2], val[1][i-2])
    print(max(val[0][count-1],val[1][count-1], val[0][count-2], val[1][count-2]))