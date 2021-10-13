import sys
input = sys.stdin.readline
n = int(input())
arr=[]
for _ in range(n):
    arr = list(input().split())
    for i in arr:
        for j in range(len(i)):
            print(i[len(i) - 1- j],end='')
        print(end= ' ')
    print()