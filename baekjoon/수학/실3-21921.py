X, N = map(int, input().split())
view = list(map(int, input().split()))
val = sum(view[0:N])
big = val
count = 1
for i in range(X - N):
    val = val - view[i] + view[i + N]
    if big < val:
        big = val
        count = 1
    elif big == val:
        count += 1
if big == 0:
    print('SAD')
else:
    print(big)
    print(count)