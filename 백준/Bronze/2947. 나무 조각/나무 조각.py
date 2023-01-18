num_list = list(map(int, input().split()))

while True:
    for n in range(4):
        
        if num_list[n] > num_list[n+1]:
            a = num_list[n]
            b = num_list[n+1]
            num_list[n] = b
            num_list[n+1] = a

            result = map(str, num_list)
            print(" ".join(result))
            

    if num_list == [1, 2, 3, 4, 5]:
        break