n = int(input())
count = int(input())
rec = list(map(int, input().split()))

candidate = dict()
for i in range(count):
    if rec[i] in candidate:
        candidate[rec[i]][0] += 1
    else:
        if len(candidate) < n:
            candidate[rec[i]] = [1, i]
        else:
            del_list = sorted(candidate.items(), key = lambda x : (x[1][0], x[1][1]))
            del_num = del_list[0][0]
            del candidate[del_num]
            candidate[rec[i]] = [1, i]
            
result = sorted(candidate.keys())

# for i in range(3):
#     print(result[i], end =' ') ##이렇게 하면 틀리고
for i in result:
    print(i, end=' ') ## 이렇게 하면 맞노,,