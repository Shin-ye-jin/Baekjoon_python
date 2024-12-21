# 단어 공부
n=list(input())
matrix=[chr(i) for i in range(ord('a'),ord('z')+1)]
matrix2=[chr(i) for i in range(ord('A'),ord('Z')+1)]

result=[0]*26
answer=[]

for i in range(len(n)):
    for j in matrix:
        if n[i]==j:
            result[matrix.index(j)]+=1
    for j in matrix2:
        if n[i]==j:
            result[matrix2.index(j)]+=1

# list.index(max(list)) 배열 원소 중 최댓값의 index()를 구하기

# 최댓값이 여러개일 경우 구하는 방법
for i in range(len(result)):
    if result[i] == max(result):
        answer.append(i)

if len(answer)>=2:
    print("?")
else:
    print(matrix2[answer[0]])