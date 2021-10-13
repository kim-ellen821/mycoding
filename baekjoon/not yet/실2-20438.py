N, K, Q, M = map(int, input().split())
sleep = list(map(int, input().split()))
check = list(map(int, input().split()))
student = [False] * (N + 3)
for i in check:
    j=1
    while i * j <= N+2:
        if i * j not in sleep:
            student[i*j] = True
            j += 1
        else:
            j += 1
            continue

for _ in range(M):
    count = 0
    s, e = map(int, input().split())
    for i in range(s, e + 1):
        if student[i] == False:
            count += 1
    print(count)