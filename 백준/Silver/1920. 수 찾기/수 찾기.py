N = int(input())
A_list = set(map(int, input().split()))
# print(A_list)
M = int(input())
numbers = map(int, input().split())

for i in numbers:
    if i in A_list:
        print(1)
    else:
        print(0)