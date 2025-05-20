# 요세푸스 문제
from multiprocessing.connection import answer_challenge

n,k = map(int,input().split())
matrix = list(range(1,n+1))
m1,m2= k-1,0
answer = []

for i in range(n):
    m2+=m1
    if m2 >= len(matrix):
        m2 = m2%len(matrix)
    answer.append(str(matrix.pop(m2)))

print("<",", ".join(answer)[:],">",sep='')

# 왜 인지는 모르나.... 초반에 0으로 나누었을때? 에러가 발생...
# 하여 비슷한 코드로 수정 시작을 k-1이 아닌 0으로 하니 잘됨
# join 사용법 !!
# %를 사용한 것, str을 사용한 것!