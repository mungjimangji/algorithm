string = input()
N = len(string)
r = N - 4
result_list = []
for i in range(1,N-1): # 첫 번째 단어는 적어도 글자 두 글자는 남겨야 한다.
    for j in range(i+1, N):
        # for k in range(j+1, N):
        word_1 = string[:i]
        word_2 = string[i:j]
        word_3 = string[j:]
        result = word_1[::-1] + word_2[::-1] + word_3[::-1]
        result_list.append(result)
result_list = sorted(result_list)
print(result_list[0])