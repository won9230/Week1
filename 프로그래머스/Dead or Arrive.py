import sys
n = int(sys.stdin.readline())
car = []
for i in range(n):
    a = list(map(int,sys.stdin.readline().split()))
    car.append([a,i+1])

car.sort()

aws = 0
for i in range(n-1):
    if car[i][0][0] != car[i+1][0][0]:
       aws += car[i][1]
aws += car[i+1][1]
print(aws)