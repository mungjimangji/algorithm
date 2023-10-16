N, M = map(int, input().split())

for i in range(N, M+1):
    check = True
    if i == 1:
        continue   

    for j in range(2, int(i**0.5)+1):
        if i % j == 0:
            check = False
            break
    if check:
        print(i)