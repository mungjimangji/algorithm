T = int(input())

for t in range(T):
    cnt = 0
    result = 0
    OX_score = input()
    for OX in OX_score:
        if OX == "O":
            cnt += 1
            result += cnt
        else:
            cnt = 0
    print(result)