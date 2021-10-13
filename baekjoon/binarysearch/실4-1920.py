def binary_search(find, start, end, arr):
    while start <= end:
        mid = (start + end) // 2
        if find == arr[mid]:
            return True
        elif find < arr[mid]:
            end = mid - 1 
        else:
            start = mid + 1
    return False

n = int(input())
arr = list(map(int, input().split()))
arr.sort()
m = int(input())
check = list(map(int, input().split()))


for i in range(m):
    find = binary_search(check[i], 0 , n - 1, arr)
    if find == True:
        print(1)
    else:
        print(0)