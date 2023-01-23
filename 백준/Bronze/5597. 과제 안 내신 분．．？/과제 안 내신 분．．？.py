import sys
students_list = []
for i in range(1, 31):
    students_list.append(i)


for _ in range(28):
    num = int(sys.stdin.readline())
    students_list.remove(num)
print(students_list[0])
print(students_list[1])