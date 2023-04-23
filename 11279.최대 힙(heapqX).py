import sys
input = sys.stdin.readline

heap = [0]
capacity = 0

def push(heap,n):
    global capacity
    if len(heap) -1 == capacity: #힙 자리가 부족할 경우
        heap = heap + [0] * len(heap) #배열을 2배로 늘린다
    
    capacity += 1 #힙 가장 뒤자리에
    heap[capacity] = n #n를 추가
    
    tn = capacity 
    while(tn > 1):
        if heap[tn] > heap[tn//2]: # 큰 숫자가 위로 올라간다
            temp = heap[tn]
            heap[tn] = heap[tn//2]
            heap[tn//2] = temp
            tn //= 2
        else:
            break
    return heap

def pop(heap):
    global capacity
    if capacity == 0: #배열이 0이면
        return 0
    p = heap[1]
    heap[1] = heap[capacity]
    heap[capacity] = 0
    
    tn = 1
    while(capacity > tn * 2): # 작은 숫자는 아래로 내려간다
        if heap[tn*2] == 0 and heap[tn * 2 + 1] == 0:
            break
        if heap[tn] < max(heap[tn*2],heap[tn*2+1]):
            temp = heap[tn]
            if heap[tn*2] > heap[tn*2+1]:
                heap[tn] = heap[tn*2]
                heap[tn*2] = temp
                tn *= 2
            else:
                heap[tn] = heap[tn*2+1]
                heap[tn*2+1] = temp
                tn = tn*2+1
        else:
            break
    capacity -= 1
    return p

for i in range(int(input())):
    x = int(input())
    if x:
        heap = push(heap,x)
    else:
        print(pop(heap))