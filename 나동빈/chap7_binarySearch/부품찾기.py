def binary_search(arr, target, start, end):
    
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return True
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return False

n = int(input())
have = list(map(int, input().split()))
m = int(input())
want = list(map(int, input().split()))

#want.sort()
have.sort()

for i in range(m):
    #print(want[i], end=' ')
    ans = binary_search(have, want[i], 0 , n - 1)

    if ans == False:
        print('no', end=' ')
    else:
        print('yes', end = ' ')
    