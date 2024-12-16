# 문자열 반복
n=int(input())

for i in range(n):
    a,m=map(str,input().split())
    a=int(a)
    re=list(m)
    for j in range(len(re)):
        print(re[j]*a,end='')
    print('') # 마지막 !! 줄바꿈