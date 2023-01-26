N = int(input())
number_list = []
for _ in range(N):
    number = int(input())
    if number == 0:
        number_list.pop()
    else:
        number_list.append(number)
print(sum(number_list))