multi = 1
result_dict = {}
for n in range(3):
    a = int(input())
    multi *= a
multi = str(multi)

for num in range(10):
    result_dict[num] = 0

for m in multi:
    m = int(m)
    if m in result_dict:
        result_dict[m] += 1
for value in result_dict.values():
    print(value)