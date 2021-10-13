num = int(input())
arr = list(map(int, input().split()))
best = max(arr)
n_arr = []
for i in range(num):
    n_arr.append(arr[i] / best * 100)
avg = sum(n_arr) / num
print(avg)