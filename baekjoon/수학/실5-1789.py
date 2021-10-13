S = int(input())

num = 1
while num*(num+1)//2 <= S:
    num +=1
print(num - 1)