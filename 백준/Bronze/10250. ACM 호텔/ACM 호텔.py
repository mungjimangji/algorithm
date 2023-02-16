for _ in range(int(input())):
    h, w, n = map(int, input().split())
    front_num = n % h
    back_num = (n // h) + 1
    if front_num == 0:
        front_num = h
        back_num -= 1
    front_num = str(front_num)
    back_num = str(back_num)
    if len(back_num) == 1:
        back_num = "0" + back_num
    print(front_num + back_num)