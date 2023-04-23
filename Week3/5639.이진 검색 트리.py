import sys
num_list = []

while True:
    try:
        num = int(sys.stdin.readline())
        num_list.append(num)
    except:
        break


def A(first,end):
    if first > end:
        return
    mid = end + 1
    for i in range(first + 1 ,end + 1):
        if num_list[first] < num_list[i]:
            mid = i
            break
    A(first+1,mid-1) #왼쪽노트
    A(mid,end)       #오른쪽노트
    print(num_list[first])
    
    
A(0,len(num_list)-1)

















# import sys
# # sys.setrecursionlimit(10**6)
# num_list = []

# while True:                               #오류가 나올떄 까지 while문을 돌려서 입력
#     try:
#         num = int(sys.stdin.readline())
#         num_list.append(num)
#     except:
#         break
    
# def postorder(first,end):                 #배열의 인덱스 값
#     if first > end: 
#         return
#     mid = end +1                          #아래에서 mid를 정해주지 못하면 사용
#     for i in range(first + 1,end + 1): 
#         if num_list[first] < num_list[i]: #왼쪽노트 오른쪽 노트 찾기
#             mid = i
#             break
#     postorder(first+1,mid-1)              #왼쪽 노드
#     postorder(mid,end)                    #오른쪽 노드
#     print(num_list[first])
    
# postorder(0,len(num_list)-1)