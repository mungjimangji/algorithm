N = int(input())
number_list = []
for n in range(1, N+1):
    a = int(input())
    number_list.append(a)

sum_number = sum(number_list)

if sum_number > N/2:
    print("Junhee is cute!")
else:
    print("Junhee is not cute!")