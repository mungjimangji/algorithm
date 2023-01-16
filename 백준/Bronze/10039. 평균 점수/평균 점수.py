a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
number_list = [a, b, c, d, e]
new_number_list = []
number_sum = 0
for number in number_list:
    if number >= 40:
        new_number_list.append(number)
    else:
        number = 40
        new_number_list.append(number)

for number in new_number_list:
    number_sum += number
print(number_sum // 5)

