# 쇠막대기
matrix = list(input())
res1 = []

num = 0
for i in range(len(matrix)):
    if matrix[i] == "(":
        res1.append("(")
    else:
        res1.pop()
        if matrix[i-1] == "(":
            num += len(res1)
        else:
            num +=1

print(num)

# ( 는  계속해서 새로운 리스트에 삽입
# )가 나왔을 경우 새로운 리스트에서 값 하나 삭제
# 삭제한 값이 ( 인 경우 ( 괄호 만큼 값 더하기 -> 여기까지는 함
# 삭제한 값이 ) 인 경우 막대의 끝이다! 해서 +1만 하기 -> 이것 주목!
