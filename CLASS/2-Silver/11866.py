# 11866 요세푸스 문제0
import sys
from collections import deque

n,k = map(int, input().split()) # 입력 받기

deq = deque([i for i in range(1, n+1)]) # 양방향 연결 리스트 생성

res = []

while len(deq) != 0: # 요세푸스 순열 생성
  for _ in range(k-1):
    deq.append(deq.popleft()) # k-1 번째 노드까지 deq 맨 뒤로 이동
  res.append(str(deq.popleft())) # k번째 노드 삭제 후 결과 배열에 추가

print('<' + ', '.join(res)+'>')

# 11866 요세푸스 문제 0

# import sys

# n,k = map(int,sys.stdin.realine().split())

# idx = 0
# queue = [i for i in range(1,n+1)]
# res = []
# while queue:
#   idx += k-1
#   if idx >= len(queue):
#     idx %- len(queue)
#   res.append(str(queue.pop(idx)))

# print("<".", ".join(res),">",sep="")