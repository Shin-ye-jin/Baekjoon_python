# 팰린드룸인지 확인하기
n=list(input())
c = True
for i in range(len(n)//2):
    if n[i] != n[len(n)-1-i]:
        c=False
        break

if c:
    print(1)
else:
    print(0)

# 길이가 5라면 0+4, 1+3 식으로 간다.
# 값이 거짓이면 break
# 참이면 1 거짓이면 0을 출력하도록 한다.