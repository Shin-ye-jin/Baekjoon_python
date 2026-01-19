# 완전제곱수
# 제곱근을 구한 뒤, 1로 나눈 나머지가 0이면 정수
# **0.5를 곱하면 루트를 씌운 것

import math
m = int(input())
n = int(input())
sum=0
min=list()

for i in range(m,n+1):
    tmp = i**0.5
    if tmp%1==0:
        sum+=i
        min.append(i)

if len(min)>0:
    print(sum)
    print(min[0])
else:
    print(-1)