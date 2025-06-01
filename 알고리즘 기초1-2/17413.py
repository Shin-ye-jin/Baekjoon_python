# 단어 뒤집기 2
# 스택 2개를 사용
# 하나씩 집어 넣으면 < 나오면 순서대로
# 아니라면 역순으로

import sys
from collections import deque

matrix = list(sys.stdin.readline().strip())

deq = deque()

pre = 0

for i in matrix:
    if i == "<": # tag<open>이라면 gat로 이 부분을 뒤집기 위함!
        pre = 1
        while deq:
            print(deq.pop(),end='')
        deq.append(i) # "<"를 집어 넣기
    elif i == ">" and pre == 1: # <>사이 문자 그대로 출력하기
        while deq:
            print(deq.popleft(),end='')
        print(i,end='') # ">" 출력
        pre = 0
    elif i == ' ' and pre == 0: # de fg -> ed gf로 반대로 하기 위함
        while deq:
            print(deq.pop(),end='')
        print(i,end='') # ' ' 공간 출력
    else:
        deq.append(i) # 그냥 알파벳일 경우 삽입만 한다!

while deq: # 아무것도 없이 알파벳으로 마무리 될 경우
    print(deq.pop(),end='')
