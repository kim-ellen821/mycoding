# n, s = map(int, input().split())
# arr = list(map(int, input().split()))
# start = 0
# end = 0
# partial_sum = 0
# small = int(1e9)

# for start in range(n):
#     while partial_sum < s and end < n:
#         partial_sum += arr[end]
#         end += 1
#     if partial_sum >= s and small > (end - start):
#             small = (end - start)
#     partial_sum -= arr[start]

# if small == int(1e9):
#     print(0)
# else:
#     print(small)

# n = 데이터의 개수, m = 구하고자 하는 부분 연속 수열의 합
n, m = 5, 5
data = [1,2,3,2,5]

count = 0
partial_sum = 0
end = 0

for start in range(n):
    # end값을 가능한 만큼 증가시킨 다음
    while partial_sum < m and end < n:
        partial_sum += data[end]
        end += 1
    
    # 부분 합이 m이라면 카운트를 증가시킨다.
    if partial_sum == m:
        count += 1
    # start값을 1 증가시키기 전에 해당 수열의 값을 빼준다.
    partial_sum -= data[start]

print(count)
