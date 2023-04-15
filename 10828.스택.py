import sys
n = int(sys.stdin.readline())

stack = []
for i in range(n):
    m = sys.stdin.readline().split()

    if m[0] == 'push':
        stack.append(m[1])
    elif m[0] == 'pop':
        if len(stack) == 0:
            print('-1')
        else :
            print(stack.pop())
    elif m[0] == 'size':
        print(len(stack))
    elif m[0] == 'empty':
        if len(stack) == 0:
            print('1')
        else :
            print('0')
    elif m[0] == 'top':
        if len(stack) == 0:
            print('-1')
        else:
            tmp = stack.pop()
            print(tmp)
            stack.append(tmp)