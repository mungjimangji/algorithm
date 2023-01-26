for _ in range(int(input())):
    string = list(input())
    result_list = []

    for s in string:
        if s == "(":
            result_list.append(s)
            
        elif s == ")":
            try:
                result_list.pop()
            except:
                result_list.append(s)
                break


    if len(result_list) == 0: 
        print("YES")
    else:
        print("NO")
