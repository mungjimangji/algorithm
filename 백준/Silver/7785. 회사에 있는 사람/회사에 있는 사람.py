import sys
result_dict = {}
result_list = []
N = int(sys.stdin.readline())
for n in range(N):
    a, b = sys.stdin.readline().split()
    result_dict[a] = b

for key in result_dict.keys():
    if result_dict[key] == "enter":
        result_list.append(key)
result_list.sort(reverse=True)

for result in result_list:
    print(result)