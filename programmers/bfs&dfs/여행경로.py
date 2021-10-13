from collections import deque

tickets = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]

# q = deque()
# for i in range(len(tickets)):
#     if tickets[i][0] == "ICN":
#         q.append((tickets[i][0], tickets[i][1]))

# while q:
#     s, e = q.popleft()
#     for i in range(len(tickets))
tickets.sort
size = len(tickets)
for i in range(size):
    if tickets[i][0] == "ICN":
        temp = tickets[i][1]
