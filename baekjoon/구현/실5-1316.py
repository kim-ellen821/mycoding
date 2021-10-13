# def check(word):
#     visited = [False] * 26
#     for i in range(len(word)):
#         temp = ord(word[i]) - 97
#         if not visited[temp]:
#             visited[temp] = True
#         elif visited[temp] and word[i - 1] == word[i]:
#             continue    
#         elif visited[temp] and word[i-1]!= word[i]:
#             return False
#     return True

# n = int(input())
# ans = 0
# for _ in range(n):
#     word = input()
#     c = check(word)
#     if c == True:
#         ans += 1
# print(ans)



#########풀이2#############
n = int(input())
count = 0
for _ in range(n):
    check = [False] * 26  
    same = False
    s = input()
    for j in range(len(s)):
        tmp = ord(s[j]) - 97
        if not check[tmp]:
            check[tmp] = True
        else:
            if s[j-1] == s[j]: continue
            else: same = True
    if not same:
        count += 1
print(count)