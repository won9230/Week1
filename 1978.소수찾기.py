n = int(input())
n1 = list()
count = 0

n1=input().split()
                
for i in range(n):
    if int(n1[i]) != 1:
        for j in range(2,int(n1[i])):
            if int(n1[i]) % j == 0:
                count += 1
                break
            else :
                a= 0
    else:
        count += 1
print(n-count)