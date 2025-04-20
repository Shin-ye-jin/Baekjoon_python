# 1966 프린터 큐
t=int(input())

for _ in range(t):
  n,m = map(int,input().split())
  data = list(map(int,input().split()))

  res = 1
  while data:
    if data[0] < max(data): # 중요도가 높은 문서가 더 있는지 확인하기 위해 max 함수 사용
      data.append(data.pop(0)) # 만약 더 중요한 문서가 있다면 0번째 문서를 pop하고 큐 맨뒤로 추가
    else:
      if m==0: break
      data.pop(0)
      res += 1

    m = m-1 if m>0 else len(data) - 1
    # m==0이지만, 이것보다 중요도가 더 높은 문서가 있다면 맨 뒤로 이동해야 하므로 m==len(큐)-1이 된다.
    # 반면 m==0이고, 이것의 중요도가 가장 높다면 해당 문서가 출력된다.

  print(res)

# 1966 프린터 큐