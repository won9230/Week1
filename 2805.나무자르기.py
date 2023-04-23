import sys
n , m = list(map(int,sys.stdin.readline().split())) #나무 개수 , 가져가는 나무 길이
tree= list(map(int,sys.stdin.readline().split()))
tree.sort()
h = 0

#높이 기준을 으로 나눈다
def bSherch(start,end):
    tmp = 0
    #start ,end 로 임시 높이를 구한다
    h = (start + end) // 2
    
    if start > end :   
        return h


    
    for i in range(n):
        if tree[i] > h:
            tmp += (tree[i] - h)
    if m == tmp:
        return h
    elif m > tmp:
        return bSherch(start,h - 1)
    elif m < tmp:
        return bSherch(h + 1,end)
    #임시 높이보다 높은 나무만 임시 높이로 빼고 총합을 구한다
    #높이랑 비교해서 리턴 or 재귀
    
print(bSherch(1,max(tree)))