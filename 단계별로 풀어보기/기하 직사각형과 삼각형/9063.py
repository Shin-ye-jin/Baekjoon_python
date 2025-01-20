# 대지
v=[]
h=[]

n=int(input())

for i in range(n):
    a,b=map(int,input().split())
    v.append(a)
    h.append(b)

m1 = max(v) - min(v)
m2 = max(h) - min(h)

print(m1*m2)