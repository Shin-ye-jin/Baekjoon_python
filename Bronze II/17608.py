# 막대기
# 왜 초창기에 했을때는 안된걸까?

from sys import stdin

n = int(stdin.readline().strip())
matrix = []
cnt,height = 0,0

for i in range(n):
    matrix.append(int(stdin.readline().strip()))

matrix.reverse()

for i in matrix:
    if i > height:
        cnt+=1
        height = i

print(cnt)