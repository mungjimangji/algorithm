import sys
# sys.stdin = open("input.txt", "r")

T = int(input())
num_list = []
for _ in range(T):
    number = int(sys.stdin.readline())
    num_list.append(number)
reuslt = []
reuslt.append(num_list.pop())

for _ in range(T-1):
    reuslt_pop = reuslt.pop()
    num_list_pop =num_list.pop()
    if reuslt_pop < num_list_pop:
        reuslt.append(reuslt_pop)
        reuslt.append(num_list_pop)
    else:
        reuslt.append(reuslt_pop)
print(len(reuslt))