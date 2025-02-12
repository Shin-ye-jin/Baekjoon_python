# 팰린드롬수

def f(n):
    for i in range(len(n)//2):
        if n[i] != n[len(n)-i-1]:
            print("no")
            return 1
    print("yes")
    return 1

while True:
    n = list(input())
    if n[0]=='0':
        break
    f(n)