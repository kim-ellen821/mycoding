import sys
input = sys.stdin.readline
N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
hap = [[0] * (N + 1) for _ in range(N + 1)]
hap[1][1] = arr[0][0]
for i in range(2, N+1):
    hap[i][1] = arr[i-1][0] + hap[i-1][1]
    hap[1][i] = arr[0][i-1] + hap[1][i-1]

for i in range(2, N+1):
    for j in range(2, N+1):
        hap[i][j] = hap[i][j-1] + arr[i-1][j-1] + hap[i-1][j] - hap[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    print(hap[x2][y2] - hap[x1-1][y2] - hap[x2][y1-1] + hap[x1-1][y1-1])
    