n = int(input())
count = 0

def a(e):
    num = list()
    d = 0
    for i in range(len(str(e))):
        num.append(str(e)[i])
    d1 = int(num[0]) - int(num[1])
    d2 = int(num[1]) - int(num[2])
    if d1 == d2:
        global count
        count = count + 1
                   
if n <= 99 :
    print(n)
else:
    for i in range(100,n+1):
        a(i)
    print(count + 99)