# 1874 스택 수열
# 1~n까지 숫자를 입력받아 수열 하나 만들기
# 입력한 수를 만날 때 까지 오름차순으로 push
# 입력한 수를 만나면 while문 탈출, 즉 cur = num일 때까지 while문을 돌아 스택을 쌓는다.
# stack의 top이 입력한 숫자와 같다면 스택의 Top을 꺼내 수열을 만들어 준다.
# stack의 top이 입력한 수가 아니면 주어진 스택을 만들 수 없다.
# 왜냐하면 12345처럼 오름차순으로 스택이 입력되는 데 top이 num보다 쿠면 num은 top보다 더 아래에 쌓여 있기 때문이다.
#
n = int(input())
stack = []
answer = []
flag = 0
cur = 1

for i in range(n):
  num = int(input())
  while cur <= num:
    stack.append(cur)
    answer.append("+")
    cur += 1

  if stack[-1] == num:
    stack.pop()
    answer.append("-")
  else:
    print("NO")
    flag = 1
    break

if flag == 0:
  for i in answer:
    print(i)