import sys
n = int(sys.stdin.readline())
stack = []
for i in range(n):
    m = int(sys.stdin.readline())
    if m == 0:
        del stack[len(stack)-1]
    else:
        stack.append(m)
    
print(sum(stack))