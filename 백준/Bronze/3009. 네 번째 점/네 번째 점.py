a, b = list(map(int,input().split()))
c, d = list(map(int,input().split()))
e, f = list(map(int,input().split()))
ace_list = [a, c, e]    
bdf_list = [b, d, f]
for i in ace_list:
    if ace_list.count(i) % 2 == 1:
        g = i
for j in bdf_list:
    if bdf_list.count(j) % 2 == 1:
        h = j
print(g, h)