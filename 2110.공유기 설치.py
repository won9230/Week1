import sys
n1 , c1 = sys.stdin.readline().split()

n = int(n1)
c = int(c1)
house = []

for i in range(n):
    house.append(int(sys.stdin.readline()))
house.sort()

start = house[0]
end = house[-1] - house[0]
result = 0

while(start <= end):
    mid = (start+end) // 2
    current = house[0]
    count = 1
    
    for i in range(1,len(house)):
        if house[i] >= current + mid:
            count += 1
            current = house[i]
    if count >= c:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)