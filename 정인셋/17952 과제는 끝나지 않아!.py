import sys
from collections import deque

n = int(sys.stdin.readline())
m = deque()
save = deque()
for i in range(n):
    m.append(list(map(int,sys.stdin.readline().split())))

main = []
aws = 0
for i in range(n):
    tmp = m.popleft()
    if tmp[0] == 0:
        if main:
            if main[2] == 0:
                if save:
                    main = save.pop()
                else:
                    continue
                main[2] -= 1
                if main[2] == 0:
                    aws += main[1]
            else:
                main[2] -= 1
                if main[2] == 0:
                    aws += main[1]
    else:
        if main:
            save.append(main)
        main = tmp
        main[2] -= 1
        if main[2] == 0:
            aws += main[1]
print(aws)