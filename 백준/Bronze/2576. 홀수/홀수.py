num_list = []
for repeat in range(7):
    num = int(input())
    if num % 2 == 1:
        num_list.append(num)
if num_list == []:
    print(-1) 
else:   
    print(sum(num_list))
    print(min(num_list))