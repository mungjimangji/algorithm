N = int(input())
string_list = []
for _ in range(N):
    string = input()
    string_list.append(string)
string_list = list(set(string_list))

string_list.sort()
string_list = sorted(string_list, key=lambda x : len(x))
for i in string_list:
    print(i)