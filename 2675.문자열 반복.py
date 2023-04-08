n = int(input())
n2 = list()
n3 = list()
n4 = list()
for i in range(n):
    n2.append(input().split())

for i in range(len(n2)):
    for j in range(len(n2[i])):
        if j == 1:
            n3.append(n2[i][j])
        else:
            n4.append(n2[i][j])

for i in range(len(n3)):
    if(i != 0):
        print('')
    for j in range(len(n3[i])):
        for k in range(int(n4[i])):
            print(n3[i][j],end='')