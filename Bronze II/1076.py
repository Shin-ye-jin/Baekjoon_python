# 저항

color = {
    "black" : '0',
    "brown" : '1',
    "red" : '2',
    "orange" : '3',
    "yellow" : '4',
    "green" : '5',
    "blue" : '6',
    "violet" : '7',
    "grey" : '8',
    "white" : '9'
}

number = [1,10,100,1000,10000,100000,1000000,10000000,100000000,1000000000]
tmp = ''

n1 = input()
tmp += color[n1]

n2 = input()
tmp += color[n2]

n3 = input()
m = int(color[n3])
res = int(tmp)*number[m]

print(res)