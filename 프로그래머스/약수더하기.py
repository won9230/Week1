def solution(arr, divisor):
    answer = []
    for i in arr :
        if not i % divisor:
            answer.append(i)
    if len(answer) != 0 :
        answer.sort()
    else:
        answer.append(-1)
    return answer