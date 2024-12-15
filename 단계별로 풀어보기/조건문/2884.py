# 알람 시계
h,m=map(int,input().split())

if m>=45:
    print(h,m-45)
else:
    m = 60+m-45
    if h>=1:
        h-=1
        print(h,m)
    else:
        h=24+h-1
        print(h,m)