import sys
from collections import deque

stack = deque()
for _ in range(int(input())):
    command = deque(sys.stdin.readline().split())

    if "push" in command:
        stack.append(command[1])
    elif "pop" in command:
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif "size" in command:
        print(len(stack))
    elif "empty" in command:
        if stack:
            print(0)
        else:
            print(1)
    elif "top" in command:
        if stack:
            print(stack[-1])
        else:
            print(-1)