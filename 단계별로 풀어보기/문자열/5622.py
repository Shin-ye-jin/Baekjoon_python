# 다이얼 !!
matrix=['ABC','DEF','GHI','JKL','MNO','PQRS','TUV','WXYZ']
n=input()
m=list(n)
cnt=0

for i in range(len(m)):
    for j in matrix:
        if m[i] in j: # 속하는가!
            cnt=cnt+matrix.index(j)+3 # 인덱스에 3을 더해서 구함

print(cnt)

# 포함되는지 확인
# 인덱스에 3을 더하기