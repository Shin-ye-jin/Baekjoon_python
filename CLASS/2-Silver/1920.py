# 수 찾기
n = int(input())
m1 = list(map(int,input().split()))

m= int(input())
m2 = list(map(int,input().split()))

s1 = set(m1) # 시간 복잡도로 중복을 제거, 복잡도 탐색하면 더 빠를 예정

for i in m2:
  if i in s1: # m2 문자열이 m1에 포함되어 있습니다.
    print(1)
  else:
    print(0)

# 1920번 - m1 수열의 수가 m2에 있는가?
