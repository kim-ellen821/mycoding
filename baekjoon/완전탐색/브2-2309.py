from itertools import combinations

dwarf = [int(input()) for _ in range(9)]
dwarf.sort()
can = list(combinations(dwarf, 7))
for a in can:
    if sum(a)==100:
        for i in a:
            print(i)
        break
