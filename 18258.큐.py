import sys,collections
n = int(sys.stdin.readline())

queue = []
dqueue = collections.deque(queue)

for i in range(n):
    m = sys.stdin.readline().split()
    if m[0]=='push':
        dqueue.append(m[1])
    elif m[0]=='pop':
        if len(dqueue) == 0:
            print('-1')
        else:
            print(dqueue.popleft())
    elif m[0] =='size':
        print(len(dqueue))
    elif m[0]=='empty':
        if len(dqueue) == 0:
            print('1')
        else:
            print('0')
    elif m[0] == 'front':
        if len(dqueue) == 0:
            print('-1')
        else:
            print(dqueue[0])
    elif m[0] == 'back':
        if len(dqueue) == 0:
            print('-1')
        else:
            print(dqueue[len(dqueue)-1])