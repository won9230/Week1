a,b = input().split()

c = list(map(int,input().split()))
d = []
for i in range(int(a)):
    if(c[i] < int(b)):
        d.append(c[i])
        
for i in range(len(d)):
    print(d[i],end=' ')