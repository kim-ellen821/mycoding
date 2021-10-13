def binary_search(array, target, start, end):
    while start<=end:
        mid = (start + end) // 2
        #찾은 경우 index값 반환
        if target==array[mid]:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

#n = 원소의 개수 target=찾고자 하는 원소
n, target = list(map(int, input().split()))
array = list(map(int, input().split()))

result = binary_search(array, target, 0, n - 1)

if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)