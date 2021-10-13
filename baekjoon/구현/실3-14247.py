# n = int(input())
# trees = list(map(int, input().split()))
# grow = list(map(int, input().split()))
# cut = []
# ans = 0
# for i in range(n):
#     cut.append([trees[i], grow[i]])

# cut.sort(key = lambda x: x[1])
# print(cut)

# for i in range(n):
#     ans += cut[i][0] + cut[i][1] * i
# # for i in range(n):
# #     cut.append(trees[i] + grow[i] * (n - 1))

# # tot = 0
# # for i in range(n):
# #     max_idx = -1
# #     max_val = 0
# #     for j in range(n):
# #         if not chopped[j] and max_val<cut[j]:
# #             max_val = cut[j]
# #             max_idx = j
# #     print(max_idx, max_val)
# #     chopped[max_idx] = True
# #     tot += max_val
# #     for j in range(n):
# #         cut[j] -= grow[j]
# print(ans)

n = int(input())
trees = list(map(int, input().split()))
grow = list(map(int, input().split()))
cut = []
ans = 0
for i in range(n):
    cut.append((trees[i], grow[i]))
cut.sort(key = lambda x: x[1])
for i in range(n):
    ans += cut[i][0] + cut[i][1] * i
print(ans)