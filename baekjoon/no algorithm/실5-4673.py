d = [True] * 10000

def self_number(num):
    number = str(num)
    for i in range(len(number)):
        num += int(number[i])
    if num < 10000:
        d[num] = False

for i in range(1, 10000):
    self_number(i)
for i in range(1, 10000):
    if d[i]:
        print(i)     
#self_number(75) 