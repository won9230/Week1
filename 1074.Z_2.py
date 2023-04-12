import sys

n,r,c = list(map(int,sys.stdin.readline().split()))
anw = 0

def d(n,r,c):
    global anw

    a = 0 #사분면
    b = pow(2,n)
    N = b * b
    if b / 2 > r and b / 2 > c:
        a = 0
    elif b / 2 > r and b / 2 <= c:
        a = 1
    elif b / 2 <= r and b / 2 > c:
        a = 2
    elif b / 2 <= r and b / 2 <= c:
        a = 3
    if n == 1:
        anw += a
        return
    if not n == 1:
        if a == 3:
            d(n-1,r-(b/2),c-(b/2))
            anw = anw + (b/2) * (b/2) * a
        if a == 2:
            d(n-1,r-(b/2),c)
            anw = anw + (b/2) * (b/2) * a
        if a == 1:
            d(n-1,r,c-(b/2))
            anw = anw + (b/2) * (b/2) * a
        if a == 0:
            d(n-1,r,c)
            anw = anw + (b/2) * (b/2) * a

d(n,r,c)
print(round(anw))