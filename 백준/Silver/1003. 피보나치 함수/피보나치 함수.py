T = int(input())
for _ in range(T):
    num = int(input())
    zero = [1, 0]
    one = [0, 1]
    
    for n in range(num+1):
        zero.append(zero[-2] + zero[-1])
        one.append(one[-2] + one[-1])
    print(zero[num], one[num])