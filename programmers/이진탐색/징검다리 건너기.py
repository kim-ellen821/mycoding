stones = [2, 4, 5, 3, 2, 1, 4, 2, 5, 1]
k = 3
def solution(stones, k):
    start, end = 1, max(stones)
    while start<=end:
        mid = (start + end) // 2
        count = 0
        for stone in stones:
            if count >= k:
                break
            elif stone - mid <= 0:
                count += 1
            elif stone - mid > 0:
                count = 0
        if count >= k:
            end = mid - 1
        elif count < k:
            start = mid + 1
    return start
ans = solution(stones, k)
print(ans)