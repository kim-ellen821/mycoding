m = str(input())

temp=[]
for i in range(len(m)):
    temp.append(m[i])
temp.sort(reverse=True)
ans=''
for i in range(len(m)):
    ans+=temp[i]
print(ans)