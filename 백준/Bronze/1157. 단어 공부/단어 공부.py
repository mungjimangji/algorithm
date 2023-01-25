alpa = input()
alpa = alpa.upper()
result_dict = {}

for i in alpa:
    if i in result_dict:
        result_dict[i] += 1
    else:
        result_dict[i] = 1

max_alpa = max(result_dict.values())

cnt = 0
for value in result_dict.values():
    if value == max_alpa:
        cnt += 1
if cnt > 1:
    print("?")
else:
    for key, value in result_dict.items():
        if value == max_alpa:
            print(key)
