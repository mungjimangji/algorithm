# 데일리 
import sys

N = int(sys.stdin.readline())
table = [list(sys.stdin.readline().split()) for _ in range(N)]

table.sort(key = lambda x: (-int(x[1]), int(x[2]), -int(x[3]), x[0]))

for student in table:
    sys.stdout.write(str(student[0]) + "\n")
#출처: https://suri78.tistory.com/109 [공부노트:티스토리]