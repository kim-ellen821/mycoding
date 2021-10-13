import sys
input = sys.stdin.readline
n, m = map(int, input().split())
tree = list(map(int, input().split()))
def find(trees, target, start, end):
    while (start<= end):
        sum = 0
        mid = (start + end) // 2
        for tree in trees:
            if mid < tree:
                sum += (tree - mid)
        if sum == target:
            return mid
        elif sum < target:
            end = mid - 1
        else:
            start = mid + 1
            best = mid
    return best
                
    
tree.sort()
#print(max(tree))
ans = find(tree, m, 0, max(tree))
print(ans)