n = input().split()
n1 = n[0]
n2 = n[1]
n3 = ''
n4 = ''
for i in n1:
    n3 = i + n3

for i in n2:
    n4 = i + n4

if(n3 <= n4):
    print(n4)
else:
    print(n3)