# 숫자 카드 2
import sys

n = int(sys.stdin.readline().strip())
n1 = list(map(int, sys.stdin.readline().strip().split()))
m = int(sys.stdin.readline().strip())
m1 = list(map(int, sys.stdin.readline().strip().split()))

dic = {}

for n in n1:
    if n in dic:
        dic[n] += 1
    else:
        dic[n] = 1

for m in m1:
    if m in dic:
        print(dic[m], end=' ')
    else:
        print(0, end=' ')