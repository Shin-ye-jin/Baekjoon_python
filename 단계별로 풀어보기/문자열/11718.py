# 그대로 출력하기
# a=input()
# b=input()
# c=input()
# print(a+"\n"+b+"\n"+c)

# 입력값이 몇 번 주어지든 간에 그대로 출력하기
# try-except 구문을 통해 입력값이 들어오면 프린트 아니면 break

while True:
    try:
        print(input())
    except EOFError:
        break