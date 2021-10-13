# #########selection sort##############
# def sel(arr):
#     for i in range(len(arr)):
#         min = arr[i]
#         flag = i    
#         for j in range(i+1, len(arr)):
#             if arr[j]<min:
#                 min = arr[j]
#                 flag = j
#         arr[i], arr[flag]= min, arr[i]
#     print(arr)

# #########insertion sort################
# def ins(arr):
#     # for i in range(1, len(arr)):
#     #     min = arr[i]
#     #     flag = i
#     #     for j in range(0, i):
#     #         if min > arr[j]:
#     #             flag = j
#     #             min = arr[j]
#     #     arr[]v

def quick(arr, start, end):
    if start>=end:
        return
    pivot = start
    left = start + 1
    right = end
    while left <= right:
        while left <= end and arr[left] <= arr[pivot]:
            left += 1
        while right > start and arr[right] >= arr[pivot]:
            right -= 1
        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
            print(left, right, end=' ')
            print('에서 엇갈림!')
            print(arr)
        else:
            arr[left], arr[right] = arr[right], arr[left]
            print(left, right, end=' ')
            print('값 교환!')
            print(arr)
    print('quicksort: arr,',end=' ')
    print(start, right -1)
    quick(arr, start, right - 1)
    print('quicksort:',end=' ')
    print(right+ 1, end)
    quick(arr, right +1, end)

arr = [5, 7, 0, 9, 3, 1, 6, 2, 4, 8]
#sel(arr)
#ins(arr)
quick(arr, 0, len(arr) - 1)
print(arr)