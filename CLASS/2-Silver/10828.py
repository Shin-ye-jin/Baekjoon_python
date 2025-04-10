# 스택
import sys
n=int(sys.stdin.readline())

stack = []

for i in range(n):
    matrix = list(sys.stdin.readline().split())

    if matrix[0] == 'push':
        stack.append(matrix[1])
    elif matrix[0] == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            a = stack.pop()
            print(a)
    elif matrix[0] == 'size':
        print(len(stack))
    elif matrix[0] == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    elif matrix[0] == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])