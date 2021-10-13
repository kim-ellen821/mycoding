s = "aabbaccc"
s1 = "ababcdcdababcdcd"
s2 = "abcabcdede"
s3 = "abcabcabcabcdededededede"
s4 = "xababcdcdababcdcd"

def solution(s):
    ans = int(1e9)
    for i in range(1, len(s)//2 + 1):
        prev = s[:i]
        comp = ''
        count = 1
        for j in range(i, len(s)+i, i):
            now = s[j : j+i]
            print(now)
            if prev == now:
                print(prev, now,end=' ')
                print('same')
                count += 1
            else:
                if count != 1:
                    print(prev, str(count), 'sum:', end=' ')
                    comp += str(count) + prev
                    print(comp)
                else:
                   print(prev, 'sum:', end=' ')
                   comp += prev
                   print(comp) 
                count = 1
                prev = now
        print(comp)
        ans = min(ans, len(comp))
        print(ans)
    return min(ans, len(s))

ans = solution('a')
print(ans)
