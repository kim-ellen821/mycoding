array = [1,5,2,6,3,7,4]
commands = [[2,5,3], [4,4,1], [1, 7, 3]]
answer =[]
for i in range(len(commands)):
    now = commands[i]
    temp = array[now[0]-1:now[1]]
    temp.sort()
    answer.append(temp[now[2] - 1])
    print(answer)
    #print(i, now[0]-1, now[1])