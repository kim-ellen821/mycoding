def solution(jobs):
    answer = []

    time = jobs[0][0] + jobs[0][1]
    num = jobs[0][2]
    answer.append(num)

    visited = [0] * len(jobs)
    visited[0] = 1
    check = True

    while check:
        if answer[-1] != num:
            answer.append(num)

        # for idx, i in enumerate(jobs):
        #     if i[0] <= time and i[2] == part and visit[idx] == 0:
        #         time = time + i[1]
        #         visit[idx] = 1
        #     elif i[0] > time:
        #         break
        for i in range(len(jobs)):
            if jobs[i[0]] <= time and jobs[i[2]]== num:
                if visited[i] == 0:
                    time += jobs[i[1]]
                    visited[i] = 1
            elif jobs[i[0]] > time:
                break

        m = {}
        # for idx, i in enumerate(jobs):
        #     if i[0] <= time and visited[idx] == 0:
        #         if i[2] not in m:
        #             m[i[2]] = i[3]
        #         else:
        #             m[i[2]] = m[i[2]] + i[3]
        for i in range(len(jobs)):
            if jobs[i[0]]<=time and visited[i] == 0:
                if jobs[i[2]] not in m:
                    m[jobs[i[2]]] = jobs[i[3]]
                else:
                    m[jobs[i[2]]] += jobs[i[3]]

        big = 0
        bignum = 0
        for i in m:
            if m[i] > big:
                big, bignum = m[i], i
            elif m[i] == big and i < bignum:
                maxpart = i

        if bignum == 0:
            for i in jobs:
                if i[0] > time:
                    bignum = i[2]
                    time = i[0]
                    break

        num = bignum

        if 0 not in visited:
            check = False

    return answer