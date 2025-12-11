# 수학은 비대면강의입니다.
# num = list(map(int,input().split()))
# tmp = []
# x,y=0,0
# for i in range(3):
#     tmp.append(num[i]*num[3])
#     tmp.append(num[i+3]*num[0])
#
# y = (tmp[4]-tmp[5])//(tmp[2]-tmp[3])
#
# x = (tmp[5]-tmp[3]*y)//tmp[1]
#
# print(x, y)

# 분모가 0이 되었을 경우 런타임 에러가 발생함 ㅠㅠ...?

# 아니 근의 공식을 사용하라니!!! 내가 어찌 기억해!!
# ax + by = p / cx + dy = q
# x = (dp - bq) / (ad - bc)
# y = (ap - cp) / (ad - bc)

import sys
a,b,c,d,e,f = map(int,sys.stdin.readline().split())

x = ((c*e) - (b*f)) // ((a*e) - (b*d))
y = ((a*f) - (c*d)) // ((a*e) - (b*d))

print(x,y)
