N = set(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

AB = A - B
BA = B - A
AB_add = AB | BA
print(len(AB_add))