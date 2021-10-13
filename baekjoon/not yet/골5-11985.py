n, m, k = map(int, input().split())
orange = [0] * (n + 1)
box = [0] * (n + 1)

for i in range(1, n + 1):
    orange[i] = int(input())
    box[i] = k * i

for i in range(n):
    small = orange[i + 1]
    big = orange[i + 1]
    for j in range(m):
        if i + j <= n:
            small = min(small, orange[i + j])
            big = max(big, orange[i + j])
            box[i + j] = min(box[i+j], box[i] + k + j * (big - small))
        
print(box)
print(box[n])