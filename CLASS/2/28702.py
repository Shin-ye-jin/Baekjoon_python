# FizzBuzz
a=input()
b=input()
c=input()
d=0

if a.isdigit() is True:
    d = int(a)+3
elif b.isdigit() is True:
    d = int(b)+2
elif c.isdigit() is True:
    d = int(c)+1

if d%3==0 and d%5==0:
    print("FizzBuzz")
elif d%3==0 and d%5!=0:
    print("Fizz")
elif d%3!=0 and d%5==0:
    print("Buzz")
else:
    print(d)