for _ in range(int(input())):
    string = input()
    a = 0
    b = 0
    for s in string:
        if s == "(":
            a += 1
        elif s == ")":
            b += 1
        if a < b:
            break
    if a == b:
        print("YES")
    else:
        print("NO")