# 손익분기점
import sys
a,b,c=map(int,sys.stdin.readline().split())

if b>=c:
    print(-1)
else:
    # while True:
    #     if (a+b*cnt) < c*cnt:
    #         print(cnt)
    #         break
    #     cnt+=1
    print(a//(c-b)+1)