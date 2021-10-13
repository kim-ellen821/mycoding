def circle(s):
    next = s[-1]
    #print('?',next)
    tmp = str(int(s[0])+ int(s[1]))
    next += tmp[-1]
    return next

n = (input())
count = 1
if len(n) == 1:
    new = '0'+ n
else: new = n
new = circle(new)
#print('한번:', new)
while int(new) != int(n):
    new = circle(new)
    #print(count,'번:', new)
    count += 1
print(count)