import sys
N = int(sys.stdin.readline())

def recursive(total_length, mid_length,N):
    if N <= 3:
        return "moo"[N-1]
       #왼쪽 수열 길이 = 가운데를 제외한 반
    left_length = (total_length - mid_length)
    
     #찾으려는 순서가 왼쪽 수열에 있으면 -> 그 전 수열로 간다
    if N <= left_length:
        return recursive(left_length,mid_length-1,N)
    
    #찾을려는 순서가 오른쪽 수열에 있으면 -> 왼쪽 수열의 순서를 바꾸고 그 전 수열로 간다
    if N > left_length + mid_length:
        return recursive(left_length,mid_length-1,N-left_length-mid_length)


    if N - left_length == 1:
        return 'm'
    else:
        return 'o'
    
total_length = 3 #moo세글자
n = 0
while total_length < N :
    n += 1
    total_length = 2 * total_length + n + 3 #기존 수열 * 2 + 'o'개수 + 'm'개수
#가운데 길이 = 수열 순서 + 3    
print(recursive(total_length,n+3,N)) #전체 수열길이,중간 수열 길이,찾아보고 싶은 수열위치