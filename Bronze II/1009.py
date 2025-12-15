# 분산처리
# import sys
# n = int(sys.stdin.readline())
#
# for i in range(n):
#     a, b = map(int, sys.stdin.readline().split())
#     tmp = a**b
#     print(tmp%10)

# ㅠㅠㅠ 역시나 역시나... 시간 초과가 발생하였도다..

import sys
n = int(sys.stdin.readline())

for i in range(n):
    a,b = map(int,input().split())
    tmp = a%10

    if tmp==0:
        print(10)
    elif tmp==1 or tmp==5 or tmp==6:
        print(tmp)
    elif tmp==4 or tmp==9:
        if b%2==0:
            print((tmp**2)%10)
        else:
            print(tmp)
    else:
        if b%4==0:
            print(tmp**4%10)
        else:
            print(tmp**(b%4)%10)

# 1의 자리 0은 10의 배수와 동일하다
# 1,5,6은 본인을 그대로 가진다.
# 4와 9는 본인과 본인을 제곱한 수를 10으로 나눈 나머지의 값을 갖는다.
# 마지막으로 2,3,7,8은 지수를 10으로 나눈 나머지를 계산
# 나머지가 0이면 그대로 출력
# 아니면 tmp를 지수만큼 제곱한 값의 나머지를 계산