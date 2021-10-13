e, s, m = map(int, input().split())
if e % 15 == 0:
    e -= 15
if s % 28 == 0:
    s-= 28
if m % 19 == 0:
    m -= 19
    
year = 1
while True:
    if year % 15 == e and year % 28 == s and year % 19 == m:
        break
    year += 1
print(year)