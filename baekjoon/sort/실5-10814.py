n = int(input())
arr = [[] for _ in range(201)]
for _ in range(n):
    person = input().split()
    age = int(person[0])
    name = person[1]
    arr[age].append(name)
for i in range(201):
    if len(arr[i])>=1:
        for j in range(len(arr[i])):
            print(i, arr[i][j])  