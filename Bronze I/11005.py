# 진법 변환 2
# 진법 변환 문제는 n이 0이 될때까지 나눈것이 가장 안전하고 빠르다.

import sys
n,b = map(int,sys.stdin.readline().split())
matrix = []
count = [chr(i) for i in range(ord('A'), ord('Z')+1)]

if n == 0:
    print(0)
else:
    while n > 0:
        res = n%b
        if res < 10:
            matrix.append(str(res)) # join을 위해 숫자를 문자로 저장한다.
        else:
            matrix.append(count[res-10])
        n = n//b

matrix.reverse()

result = "".join(matrix)
print(result)