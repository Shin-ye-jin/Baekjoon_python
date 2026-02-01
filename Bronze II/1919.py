# 애너그램 만들기
tmp1 = list(input())
tmp2 = list(input())
# 리스트 형태로 입력 받기

n1 = len(tmp1)
n2 = len(tmp2)
# 길이 확인

cnt=0

for i in tmp1: # tmp1에서 하나씩 가져오기
    if i in tmp2: # tmp1에서 가져온게 tmp2에 있는가?
        tmp2.remove(i) # tmp2에서 삭제한다.
        cnt+=1 # 삭제한 것 개수 세기

print(n1-cnt+len(tmp2)) # tmp2는 삭제 당한 것에서 남은 길이만 빼기