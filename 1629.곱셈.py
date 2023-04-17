import sys

a,b,c = map(int,sys.stdin.readline().split())

def Dac(_a,_b):
    if _b == 1:
        return _a % c
    
    temp = Dac(_a,_b//2)
    
    if _b % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * _a % c
    
print(Dac(a,b))