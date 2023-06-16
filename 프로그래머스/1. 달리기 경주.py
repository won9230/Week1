import sys

def solution(players, callings):
    answer = []
    a = {player : i for i, player in enumerate(players)}
    b = {i : player for i, player in enumerate(players)}
    
    for call in callings:
        cur_id = a[call]
        pre_id = cur_id - 1
        cur_player = call
        pre_player = b[pre_id]
        
        a[cur_player] = pre_id
        a[pre_player] = cur_id
        
        b[pre_id] = cur_player
        b[cur_id] = pre_player
         
    return list(b.values())

players = sys.stdin.readline().rstrip().split()
callings = sys.stdin.readline().rstrip().split()

print(solution(players,callings))
