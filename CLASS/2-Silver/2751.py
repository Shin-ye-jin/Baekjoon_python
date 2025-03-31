# 수 정렬하기 2
import sys

n=int(sys.stdin.readline())
matrix = []

for i in range(n):
    matrix.append(int(sys.stdin.readline()))

for i in sorted(matrix):
    print(i)


# sorted와 sort의 차이..?
# int를 사용하니 된다..?