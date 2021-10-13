# bridge_length = 2
# weight = 10
# truck_weights = [7, 4, 5, 6]

# bridge_length = 100
# weight = 100
# truck_weights = [10]

bridge_length = 100
weight = 100
truck_weights = [10,10,10,10,10,10,10,10,10,10]

from collections import deque

def solution(bridge_length, weight, truck_weights):
    # answer = 0
    # q = deque()
    # tmp = 0
    # while q:
    #     for i in range(len(truck_weights)):
    #         if tmp + truck_weights < weight and len(q) < bridge_length:
    #             tmp += truck_weights[i]
    #             q.append((i, truck_weights[i]))
    #             #q에 넣는 만큼 이동한 거?
    #             #answer += 1
    #         else:

    answer = 1
    q = deque(0 for _ in range(bridge_length - 1))
    now = truck_weights[0]
    q.append(truck_weights.pop(0))

    while q:
        #for i in range(len(q)):
        #    now += q[i]
        if len(q) == 1 and len(truck_weights) == 0:
            return answer + 1
        else:
            answer += 1
            out = q.popleft()
            now -= out
            if len(truck_weights)!= 0:
                if now + truck_weights[0] <= weight:
                    now += truck_weights[0]
                    q.append(truck_weights.pop(0))
                else:
                    q.append(0)          

ans = solution(bridge_length, weight, truck_weights)
print(ans)