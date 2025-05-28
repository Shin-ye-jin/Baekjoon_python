# 학점 계산
a = {"A+":4.3,"A0":4.0,"A-":3.7}
b = {"B+":3.3,"B0":3.0,"B-":2.7}
c = {"C+":2.3,"C0":2.0,"C-":1.7}
d = {"D+":1.3,"D0":1.0,"D-":0.7}
f = 0.0
n = input()

if n in a.keys():
    print(a[n])
elif n in b.keys():
    print(b[n])
elif n in c.keys():
    print(c[n])
elif n in d.keys():
    print(d[n])
else:
    print(f)

# 딕셔너리 사용!!