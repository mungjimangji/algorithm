N = int(input())
num_list = list(map(int, input().split()))
r_list = []
a = 0
result = 0
for n in range(N-1):

    if num_list[n] < num_list[n+1]:
        r_list.append(num_list[n])
        r_list.append(num_list[n+1])
    
        if n+1 == N-1:
            if len(r_list) > 0:
                a = r_list.pop() - r_list[0]
                if result < a:
                    result = a

    elif num_list[n] >= num_list[n+1] or n+1 == N-1:
        try:
            a = r_list.pop() - r_list[0]

            if result < a:
                result = a
            r_list.clear()
        except:
            pass
    

print(result)