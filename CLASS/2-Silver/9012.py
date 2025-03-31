# 괄호
def f(n):
  match = {')':'('}
  list = []
  answer = 'YES'

  for i in n:
    if i == '(':
      list.append(i)
    else:
      if not len(list):
        answer = 'NO'
        break
      top = list.pop()

      if match[i] != top:
        answer = 'NO'
        break
  if len(list):
    answer = 'NO'
  return answer

n = int(input())

for i in range(n):
  n=input()
  print(f(n))

# 9012번