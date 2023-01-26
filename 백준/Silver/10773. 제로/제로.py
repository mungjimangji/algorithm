T = int(input())
money_list = []
for _ in range(T):
    N = int(input())
    money_list.append(N)

new_money_list = []

for money in money_list:
    if money == 0:
        new_money_list.pop()
    else:
        new_money_list.append(money)
print(sum(new_money_list))
