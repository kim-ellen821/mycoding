tot = input()
part = input()

print(int(part in tot))
# totsize = len(tot)
# chksize = len(part)
# check = [False] * chksize

# for i in range(totsize):
#     if tot[i] == part[0]:
#         if i + chksize > totsize:
#             break
#         else:
#             for k in range(len(part)):
#                 if tot[i + k] == part[k]:
#                     check[k] = True
# count= 0
# for i in range(len(part)):
#     if check[i] == True:
#         count +=1
# if count == len(part):
#     print(1)
# else:
#     print(0)