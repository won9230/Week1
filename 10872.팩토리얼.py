n = int(input())

def pa(a):   
    if a == 0:
        return 1
    elif a >= 1:
        return  a * pa(a-1)
    
print(pa(n))