T = int(input())
result = 0
for _ in range(T):
    string = input()
    result_list = []
    
    for s in range(len(string)):
        if string[s] not in result_list:
            result_list.append(string[s])
            cnt = 1
        else:
            if string[s] == string[s-1]:
                continue
            else:
                cnt = 0
                break       
    result += cnt
print(result)
