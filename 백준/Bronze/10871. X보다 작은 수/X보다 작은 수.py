N, X = map(int, input().split())
number_list = map(int, input().split())

for number in number_list:
    if number < X:
        print(number, end=" ")
    else:
        continue