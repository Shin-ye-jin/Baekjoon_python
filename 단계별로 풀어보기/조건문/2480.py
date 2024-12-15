# 주사위 세개 !!!
a,b,c=map(int,input().split())
if a==b==c:
    print(10000+a*1000)
elif a==b or a==c:
    print(1000+a*100)
elif b==c:
    print(1000+b*100)
else:
    print(max(a,b,c)*100)

# 1번 다 같은 경우
# 첫 번째 숫자와 같은 경우
# 두 번째 숫자와  세 번재 숫자가 같은 경우
# 모두 다 다른 경우