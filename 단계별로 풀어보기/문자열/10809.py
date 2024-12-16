# 알파벳 찾기
S = list(input())
c = 'abcdefghijklmnopqrstuvwxyz'

for i in c:
    if i in S:
        print(S.index(i), end=' ')
    else:
        print(-1,end=' ')

# for문을 이용하여 a부터 Z까지 알파벳이 있는지 검사한다.
# 있으면 인덱스를 출력
# 없으면 -1을 출력