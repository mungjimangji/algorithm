S = input()
result_list = [-1]*26
for s in S:
    s_index = S.index(s)
    s_ord = ord(s) - 97
    result_list[s_ord] = s_index
for result in result_list:
    print(result, end=" ")