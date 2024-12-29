# 크로아티아 알파벳 !!
matrix = ['c=','c-','dz=','d-','lj','nj','s=','z=']

n=input()

for i in matrix:
    n = n.replace(i,'*')
print(len(n))

# input() 변수와 동일한 이름의 변수
# replace 함수로 수정된 문자를 입력받은 변수와 동일한 변수에 선언하는 경우

# 입력을 받아 와서 꺼내 와서 존재하면 "*"로 바꾼다.
