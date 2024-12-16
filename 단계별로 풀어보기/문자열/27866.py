# 문자와 문자열
s=input()
n=int(input())
n-=1
re=list(s)
for i in range(len(re)):
    if i==n:
        print(re[i])