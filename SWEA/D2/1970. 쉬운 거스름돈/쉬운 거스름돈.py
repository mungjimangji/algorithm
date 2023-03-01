T = int(input())
for t in range(1, T+1):
    money = int(input())
    money_list = [50000, 10000, 5000, 1000, 500, 100, 50, 10]
    result = []
    for m in money_list:
        a = money // m
        result.append(a)
        money -= m * a
    print(f"#{t}")
    print(*result)
