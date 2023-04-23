import sys
from collections import deque
_n = sys.stdin.readline()
n = _n.strip()
stack = []
stack = deque(stack)
p = 1 #P확인
a = 0 #A확인
for i in n:
    stack.append(i)
    if i != 'P':
        a += 1
if stack[len(stack)-1] == 'A':
    print('NP')
else:
# 문자열을 스택에 넣고
# PPAP는 A를 기준으로 앞에 2개 뒤에 1개의 P가 있다
# A가 나올때 마다 P를 2개 씩 늘린다.
    while True:
        x1 = stack.pop()
        #stack에서 꺼낸게 P인지 A인지 확인
        if x1 == 'P':
            p -= 1    #P면 p - 1
        else:         #A면 p + 2 and a - 1
            p += 2
            a -= 1
        
        if p < 0 or a < 0:
            print('NP')
            break
        
        if len(stack) == 0:
            if p == 0 and a == 0:
                print("PPAP")    #스택의 길이가 0일떄 p하고 a가 0이면 PPAP출력
                break
            else:
                print('NP')      #아니면 NP출력
                break
        else:
            x2 = stack.pop()
            if x1 == 'A'and x2 == 'A':
                print('NP')
                break
            else:
                stack.append(x2)