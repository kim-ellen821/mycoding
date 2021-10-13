# n = 8
# k = 2
# cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z"]

n = 8
k = 2
cmd = ["D 2", "C", "U 3", "C", "D 4", "C", "U 2", "Z", "Z", "U 1", "C"]


def solution(n, k, cmd):
    arr = []
    q = []
    
    for i in range(n):
        arr.append([i, True])
    #print(arr[0][0], arr[0][1])
    print(arr)
    

    for i in cmd:
        if len(i) == 3:
            if i[0] == "D":
                for j in range(int(i[2])):
                    if k + 1 >= n:
                        k -= n
                    if arr[k+1][1] == True:
                        k += 1
                    elif arr[k+1][1] == False:
                        if k + 2 >= n:
                            k -= n
                        k += 2
                            
                print('D:', end='')
                print(k)
            if i[0] == "U":                
                for j in range(int(i[2])):
                    if k - 1 < 0:
                        k += (n-1)
                    if arr[k - 1][1] == True:
                        k -= 1
                    elif arr[k-1][1] == False:
                        if k - 2 < 0:
                            k += (n-1)
                        k -= 2
                        print('2up')
                print('U:', end='')
                print(k)
        elif i == "C":
            arr[k][1] = False
            q.append(k)
            if k == n - 1:
                k -= 1
            else:
                k += 1
                if k >= n:
                    k -= n
            print('C:', end='')
            print(k)

        elif i == "Z":
            n = q.pop()
            arr[n][1] = True
            if n <= k:
                k += 1
            print('Z:', end='')
            print(k)
            
    answer = ''        
    for i in range(len(arr)):
        if arr[i][1] == True:
            answer+='O'
        else:
            answer+='X'
    
    return answer

s = solution(n, k, cmd)
print(s)