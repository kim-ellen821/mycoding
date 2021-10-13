n = int(input())

array =[]
for _ in range(n):
    a = int(input())
    array.append(a)

array.sort()
for i in range(n):
    print(array[i])