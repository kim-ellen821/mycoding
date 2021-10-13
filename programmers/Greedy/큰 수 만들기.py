# number = "1924"
# k = 2
# number = "1231234"
# k = 3
number = "4177252841"
k = 4
from itertools import combinations
def solution(number, k):
    answer=''
    new = list(number)
    nums = set()
    nums |= set(map(''.join, combinations(new, len(new) - k)))
    print(nums)
    max = []
    
    #answer = str(max(nums))
    return answer

ans = solution(number, k)
print(ans)