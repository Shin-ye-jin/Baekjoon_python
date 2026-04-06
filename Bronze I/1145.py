# 적어도 대부분의 배수
# 3개씩 조합할 수 있는 모든 경우를 따져서 그 중 가장 작은 숫자 찾기
# 입력되는 숫자가 100이하로 작다.
# 해서 브루트 포스(모든 경우 다 해보기)로 아주 쉽게 풀 수 있음
# 나누어 떨어지는 개수가 3개 이상이 되는 순간 그 n이 바로 정답

import sys

matrix = list(map(int, sys.stdin.readline().split()))

n = 1

while True:
    cnt = 0
    for i in range(5):
        if n % matrix[i] == 0:
            cnt+=1

    if cnt >= 3:
        print(n)
        break

    n += 1