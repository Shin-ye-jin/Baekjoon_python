#중앙 이동 알고리즘
n=int(input())
m=2

for i in range(n):
    m=m+2**i

print(m*m)