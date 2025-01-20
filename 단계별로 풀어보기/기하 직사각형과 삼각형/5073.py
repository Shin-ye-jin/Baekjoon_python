# 삼각형과 세 변
def f(a,b,c):
    sum=a+b+c
    m = max(a,b,c)

    if m<(sum-m):
        if a==b and b==c and c==a:
            print("Equilateral")
        elif a==b or b==c or c==a:
            print("Isosceles")
        else:
            print("Scalene")
    else:
        print("Invalid")

while True:
    a,b,c=map(int,input().split())
    if a==0 and b==0 and c==0:
        break
    f(a,b,c)
