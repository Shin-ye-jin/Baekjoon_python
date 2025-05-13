# 단어 뒤집기 (전체)
# import sys
# n=int(input())
# stack = []
# for i in range(n):
#     matrix = list(sys.stdin.readline().rstrip())
#
#     for j in range(len(matrix)):
#         stack.append(matrix[j])
#
#     for j in range(len(stack)):
#         print(stack.pop(),end='')

# 단어 뒤집기
import sys
n = int(input())
stack = []

for i in range(n):
    matrix = list(sys.stdin.readline().rstrip().split())

    for i in matrix:
        print(i[::-1],end=' ') # [::-1] 이게 역순 출력
