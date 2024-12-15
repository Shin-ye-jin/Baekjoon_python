# A+B -4
while True:
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break

# 테스트 케이스가 얼마나 들어올지 모르는 상황
# 이런 경우에 try, except으로 테스트 케이스가 들어오지 않을 때
# except의 break로 while 문을 종료