# 덱
# 1번 돌아가긴 하나 시간 초과
# n = int(input())
# matrix = []
#
# for i in range(n):
#     cm = input().split()
#
#     if cm[0] == "push_back":
#         matrix.append(cm[1])
#     elif cm[0] == "push_front":
#         matrix.insert(0,cm[1])
#     elif cm[0] == "front":
#         if len(matrix) > 0:
#             print(matrix[0])
#         else:
#             print(-1)
#     elif cm[0] == "back":
#         if len(matrix) > 0:
#             print(matrix[-1])
#         else:
#             print(-1)
#     elif cm[0] == "pop_front":
#         if len(matrix) > 0:
#             print(matrix[0])
#             del matrix[0]
#         else:
#             print(-1)
#     elif cm[0] == "pop_back":
#         if len(matrix) > 0:
#             print(matrix.pop())
#         else:
#             print(-1)
#     elif cm[0] == "size":
#         print(len(matrix))
#     elif cm[0] == "empty":
#         if len(matrix) == 0:
#             print(1)
#         else:
#             print(0)

# 덱 사용해서 수정
# 덱 사용하니 시간 초과 안남!!
from collections import deque
import sys

n = int(input())
matrix = deque()

for i in range(n):
    cm = sys.stdin.readline().split()

    if cm[0] == "push_back":
        matrix.append(cm[1])
    elif cm[0] == "push_front":
        matrix.appendleft(cm[1])
    elif cm[0] == "front":
        if matrix:
            print(matrix[0])
        else:
            print(-1)
    elif cm[0] == "back":
        if matrix:
            print(matrix[len(matrix)-1])
        else:
            print(-1)
    elif cm[0] == "pop_front":
        if matrix:
            print(matrix[0])
            matrix.popleft()
        else:
            print(-1)
    elif cm[0] == "pop_back":
        if matrix:
            print(matrix[len(matrix)-1])
            matrix.pop()
        else:
            print(-1)
    elif cm[0] == "size":
        print(len(matrix))
    elif cm[0] == "empty":
        if matrix:
            print(0)
        else:
            print(1)