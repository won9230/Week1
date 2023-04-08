import math

n = int(input())
n1 = list()
n2 = list()


for i in range(n):
     n1.append(int(input()))


def minority(a):
    for i in range(2,int(math.sqrt(a)+1)):
        if a % i == 0:
            return False
    return True

for i in range(n):
    A = int(n1[i] / 2)
    B = int(A)
    c = int(n1[i]/2)
    for j in range(c):    
        if minority(A) and minority(B):
            print(str(A)+' '+str(B))
            break
        else:
            A -= 1
            B += 1
