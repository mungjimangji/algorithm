number_list = []
for n in range(9):
    number = int(input())
    number_list.append(number)

print(max(number_list))
print(number_list.index(max(number_list))+1)