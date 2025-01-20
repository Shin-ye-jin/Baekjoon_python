# 네 번째 점
v = []
h = []

for i in range(3):
    a,b=map(int,input().split())
    v.append(a)
    h.append(b)

if v.count(max(v)) == 1:
    if h.count(max(h)) == 1:
        print(max(v),max(h))
    else:
        print(max(v),min(h))
else:
    if h.count(max(h)) == 1:
        print(min(v),max(h))
    else:
        print(min(v),min(h))