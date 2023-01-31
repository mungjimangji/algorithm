from collections import Counter

num_list = []
for _ in range(10):
    num = int(input())
    num_list.append(num)
num_dict = Counter(num_list)
num_avg = sum(num_list) // len(num_list)
result = num_dict.most_common(1)
print(num_avg)
print(result[0][0])