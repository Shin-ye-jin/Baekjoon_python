# 최소공배수
import sys
input = sys.stdin.readline

a = int(input())
res = 0

for i in range(a):
    x,y = map(int,input().split())

    for j in range(1,y+1):
        if x%j==0 and y%j==0:
            res = j*(x//j)*(y//j)

    print(res)