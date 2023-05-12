import sys

def sol(n,i,j):
    if n == 0:
        return
    
    cnt = (j - i + 1) // 3
    sol(n - 1,i ,i + cnt - 1)
    for k in range(i + cnt, i + cnt * 2):
        ans[k] = ' '
    sol(n - 1, i + cnt * 2, i + cnt * 3 - 1)
    
while True:
    try:
        n = int(sys.stdin.readline())
        ans = ['-'] * (3 ** n)
        sol(n,0,3 ** n - 1)
        print(''.join(ans))
    except:
        break