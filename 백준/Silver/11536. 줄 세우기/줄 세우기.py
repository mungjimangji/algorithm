n = int(input())
 
li = []
 
for _ in range(n):
    name = input()
    li.append(name)

if sorted(li) == li:
    print("INCREASING")
elif sorted(li, reverse=True) == li:
    print("DECREASING")
else:
    print("NEITHER")