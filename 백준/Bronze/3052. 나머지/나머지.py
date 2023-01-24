num_set = set()
for _ in range(10):
    num = int(input())
    num = num % 42
    num_set.add(num)
print(len(num_set))