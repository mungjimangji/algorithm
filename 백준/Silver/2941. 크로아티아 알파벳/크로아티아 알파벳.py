croa_list = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=","z="]

string = input()

for i in croa_list:
    if i in string:
        string = string.replace(i, "1")
print(len(string))
