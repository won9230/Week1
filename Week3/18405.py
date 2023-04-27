import sys
from collections import deque

n,k = map(int,sys.stdin.readline().split())
s,x,y = map(int,sys.stdin.readline().split())
graph = [list(map(int,sys.stdin.readline().split())) for _ in range(n)] 