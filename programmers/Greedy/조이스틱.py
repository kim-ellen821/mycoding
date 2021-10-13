#name = 'JAN'
#name = 'JEROEN'
#name = 'BBBAAAB'
name = 'ABABAAAAABA'
ans = 0
a_list = []
for i in name:
    count = min(ord(i) - ord('A'), ord('Z') - ord(i) + 1)
    ans += count

size = len(name)
# 'A' 위치 리스트 만들기
for i in range(size):
    if name[i] =='A':
        if i == 0 or name[i-1]!='A':
            a_list.append(i)
        if i == size - 1 or name[i+1]!='A':
            a_list.append(i)

# if not a_list:
#     ans += len(name) - 1
# else:
#     print(a_list)
#     if a_list[0] == 0:
#         ans += size - a_list[1]
#     else:
#         small = min((a_list[0] - 1) * 2 + size - a_list[1] - 1, size - 1)
#         print('path:',end='')
#         print(small)
#         ans += small
cost = []
#왔다갔다 안 할때 정방향으로..
cost.append(size - 1)

print(a_list)
for i in range(0, len(a_list)):
    if i % 2 == 1: continue
    #print(a_list[i])
    if a_list[i] == 0:
        #ans += size - a_list[1]
        temp = size - a_list[i + 1] - 1
        cost.append(temp)
    else:
        temp = (a_list[i] - 1) * 2 + size - a_list[i+1] - 1
        #print('path:',end='')
        #print(small)
        cost.append(temp)
small = min(cost)
ans += small       
print(ans)