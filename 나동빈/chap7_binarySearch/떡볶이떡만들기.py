
def binaryFind(arr, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        sum = 0
        for i in range(4):
            if arr[i] > mid:
                sum += (arr[i] - mid)
        if sum == target:
            #print(mid, end=' ')
            return mid
        if sum > target:
            #치명적 실수!!!!
            #target 값에 정확히 도달하지 못하였을 때 값을 저장하는걸 생각했어야함
            result = mid
            start = mid + 1
        elif sum < target:
            end = mid - 1
    #
    #result에 대한 구현을 생각못했었다!        
    return result


n, m = map(int, input().split())

rcake = (list(map(int, input().split())))

#rcake.sort()
end = max(rcake)
#아래의 방법은 sort를 이용하기 때문에 위의 것이 나을것같음,,
ans = binaryFind(rcake, m, 0, end)
#치명적인실수!!!!시작점을 0으로 해야지! rcake의 가장 작은 값이 아니라
#ans = binaryFind(rcake, m, rcake[0], rcake[n - 1])
print(ans)