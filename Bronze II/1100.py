# 하얀 칸
# 체스판 색상 규칙 하얀칸 : r+c가 짝수인 칸
# 체스판 색상 규칙 검정칸 : r+c가 홀수인 칸
# (0,2)이면 짝수 (1,4)이면 홀수

sum=0

for i in range(8):
    matrix = list(input())
    for j in range(8):
        if matrix[j] == 'F' and (i+j)%2==0:
            sum+=1

print(sum)


