n = int(input())
c = list()
a = 0
sum = list()
average = list()

for i in range(n):
    c.append(input().split())

for i in range(len(c)):
    a = 0
    for j in range(len(c[i])-1):
        a += float(c[i][j+1])
    a = a / float(c[i][0])
    sum.append(a)
    
for i in range(len(c)):
    b = 0
    for j in range(len(c[i])-1):
        if(sum[i] < float(c[i][j+1])):
            b += 1
    average.append((b/float(c[i][0])*100))
    
for i in range(len(average)):
    f = round(float(average[i]),3)
    print(format(f,'.3f') + '%')