a = int(input())
b = int(input())
c = int(input())

d = a*b*c

e = list()

f = 0
strD = str(d)

for i in range(10):
    f = 0
    for j in range(len(strD)):
        if(int(strD[j]) == i):
            f += 1
    e.append(f)

for i in range(len(e)):
    print(e[i])