from bisect import bisect_left,bisect_right
# citations = [3,0,6,1,5]
citations = [1,3,1]
# citations = [1233,311,111]

citations.sort()
for i in range(len(citations)):
    answer = citations[i]
    if i >= citations[len(citations) - 1 - i]:
        break
    if i == len(citations) - 1:
        i += 1
    
print(i)