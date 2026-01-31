# 문자열 분석
import sys

while True:
    try: # EOF 예외 처리
        matrix = list(input())
        up, lo, num, b = 0, 0, 0, 0
        for str in matrix:
            if str.isupper(): # 문자가 소문자인지 판별한다.
                up+=1
            elif str.islower(): # 문자가 대문자인지 판별한다.
                lo+=1
            elif str.isdigit(): # 문자가 숫자인지 판별한다.
                num+=1
            elif str == ' ': # 문자가 공백인지 판별한다.
                b+=1
        print(lo,up,num,b)
    except:
        break