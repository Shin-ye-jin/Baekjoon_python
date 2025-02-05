# 웰컴 키트
n=int(input())
matrix=list(map(int,input().split()))
t,p = map(int,input().split())
s1,s2=0,0

for i in range(len(matrix)):
    s1+=matrix[i]
    if matrix[i] % t !=0:
        s2+=1
    s2+=(matrix[i]//t)

re = s1//p

print(s2)
print(re,s1-re*p)




# 23
# 3 1 4 1 5 9
# 5 7
# -> 5장씩 1 1 1 1 1 2 총 7 묶음
# -> 7자루씩 3묶음과 ! 2개가 남으니 한자루씩 2개 주문!
# 7
# 3 2