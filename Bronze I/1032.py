# 명령 프롬프트

import sys
n = int(input())
matrix = []


for i in range(n):
    matrix.append(input())

for res in zip(*matrix):
    if len(set(res)) == 1:
        print(res[0],end='')
    else:
        print('?',end='')

# zip 함수가 아닌 range를 쓰면 문자열을 숫자로 바꿀 수 없다라는 에러 발생
# zip : 여러 개의 리스트(뜨는 반복 가능한 객체)를 받아서 같은 인덱스에 있는 요소들끼리 짝을 지어주는 역할