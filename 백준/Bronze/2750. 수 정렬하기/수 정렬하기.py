N = int(input())
num_list = []
for n in range(N):
    a = int(input())
    num_list.append(a)
num_list.sort()
for num in num_list:
    print(num)
