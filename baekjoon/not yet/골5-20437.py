import sys
input = sys.stdin.readline

T = int(input())
alpha = [[] for _ in range(26)]
for _ in range(T):
    W = input().rstrip()
    K = int(input())
    short = int(1e9)
    longest = -1
    for i in range(len(W)):
        alpha[ord(W[i]) - 97].append(i)
    for i in range(26):
        size = len(alpha[i])
        if size>= K:
            for j in range(size - K + 1):
                tmp = alpha[i][j + K - 1] - alpha[i][j] + 1
                if tmp < short:
                    short = tmp
                elif tmp > longest:
                    longest = tmp
    if short> longest:
        print(-1)
    else:
        print(short, longest)