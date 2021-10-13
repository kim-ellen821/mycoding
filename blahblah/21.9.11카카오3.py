fees, records = [180, 5000, 10, 600], ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT", "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN", "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"]
enter = dict()
exit = dict()

import math
def time(s):
    h, m ='',''
    h += s[0] + s[1]
    m += s[3] + s[4]
    return (int(h) * 60 + int(m))
answer= []
for record in records:
    event = record.split()
    if event[2] =='IN':
        if event[1] in enter:
            enter[event[1]].append(time(event[0]))
        else:
            enter[event[1]] = [time(event[0])]
    elif event[2] == 'OUT':
        if event[1] in exit:
            exit[event[1]].append(time(event[0]))
        else:
            exit[event[1]] = [time(event[0])]
enter_s = sorted(enter.keys())

print(enter, exit)
for rec in enter_s:
    cost, tot_time = 0, 0
    #for i in enter.get(rec):
        #print(i)
    print('now:',rec)
    for i in range(len(enter[rec])):
        count = 0
        if rec in exit and len(exit[rec]) > i:
            print('enter, exit:',enter[rec][i], exit[rec][i])
            count = exit[rec][i] - enter[rec][i]
        else:
            count = 1439 - enter[rec][i]
        tot_time += count
    print('tot:',tot_time)

    if tot_time <= fees[0]:
        cost = fees[1]
    else:
        tmp = math.ceil((tot_time - fees[0])/fees[2])
        cost = fees[1] + tmp * fees[3]
    answer.append(cost)
print(answer)