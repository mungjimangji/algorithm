w_uni = []
k_uni = []
for _ in range(10):
    w = int(input())
    w_uni.append(w)
for _ in range(10):
    k = int(input())
    k_uni.append(k)
w_uni.sort()
k_uni.sort()
w_result = 0
k_result = 0

for i in w_uni[-3:]:
    w_result += i
for j in k_uni[-3:]:
    k_result += j
print(w_result, k_result)