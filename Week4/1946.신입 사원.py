import sys
t = int(sys.stdin.readline())

for k in range(t):
    n = int(sys.stdin.readline())
    people = []
    cnt = 1
    for i in range(n):
        people.append(list(map(int,sys.stdin.readline().split())))
    people.sort(key=lambda x :(x[0],x[1]))
    top = people[0][1]
    for i in range(n):
        if top > people[i][1]:
            top = people[i][1]
            cnt += 1
    print(cnt)