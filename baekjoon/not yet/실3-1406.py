import sys
input = sys.stdin.readline
org = input()
point = 0
n = int(input())
for _ in range(n):
    cmd = input()
    print(cmd)
    if cmd == 'L':
        if point == 0: continue
        else: point -= 1
    elif cmd =='D':
        if point == len(org): continue
        else: point += 1
    elif cmd =='B':
        if point == 0: continue
        else: 
            del org[point - 1]
            point -= 1
    elif cmd[0] =='P':
        org.insert(point, cmd[2])
print(org)