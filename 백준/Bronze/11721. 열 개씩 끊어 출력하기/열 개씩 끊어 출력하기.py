word = input()
len_word = len(word)
repeat_num = len_word // 10
last_word = len_word % 10
for n in range(0,repeat_num):
        result = word[10*n : 10*(n+1)] # 0:10 / 10:20 / 20:30 
        print(result)
if last_word != 0:
    print(word[-last_word:])