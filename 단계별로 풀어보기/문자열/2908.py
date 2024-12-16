# 상수
a,b=map(str,input().split())
n1=list(a)
n2=list(b)

n1.reverse()
n2.reverse()

m1,m2='',''

for i in range(3):
    m1 = m1+n1[i]
    m2 = m2+n2[i]

if int(m1)>int(m2):
    print(m1)
else:
    print(m2)