T = int(input())
result_list = []
for t in range(T):
    sentence = input().split()

    for word in sentence:
        result_list.append(word[::-1])
        
    print(" ".join(result_list))
    result_list = []