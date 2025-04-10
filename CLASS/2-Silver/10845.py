# 큐
import sys
n=int(sys.stdin.readline())

queue = []

for i in range(n):
    matrix = list(sys.stdin.readline().split())

    if matrix[0] == 'push':
        queue.append(matrix[1])
    elif matrix[0] == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            a = queue.pop(0)
            print(a)
    elif matrix[0] == 'size':
        print(len(queue))
    elif matrix[0] == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    elif matrix[0] == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    elif matrix[0] == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])