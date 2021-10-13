def solution(money, minratio, maxratio, ranksize, threshold, months):
    money = int(str(money)[:-2]) * 100
    for _ in range(months):
        while minratio <= maxratio:
            if money<threshold:
                break
    print(money)

solution(12345678, 10, 20, 250000, 13345678, 4)