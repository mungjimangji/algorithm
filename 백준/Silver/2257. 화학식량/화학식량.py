string = input()
alpa_dict = {"H":1, "C":12, "O":16}
stack = []

for s in string:
    if s == "(":
        stack.append(s)
        # print(stack)

    elif s == ")":
        result = 0

        while True: # 스택 돌아주기
            cur = stack.pop()
            if cur == "(": # 열린괄호만 나오면 종료
                break
            # print(stack)
            result += cur
        stack.append(result)
        # print(stack)

    elif s in alpa_dict:
        stack.append(alpa_dict[s])
        # print(stack)
    # 숫자이면
    else:
        stack[-1] *= int(s)
print(sum(stack))