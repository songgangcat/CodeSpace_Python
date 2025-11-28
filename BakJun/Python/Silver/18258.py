import sys
from collections import deque
input = sys.stdin.readline

que = deque()
N = int(input())

for _ in range(N):
    order, *rest = map(str, input().split())
    if order == "push":
        que.append(rest[0])
    elif order == "pop":
        print(que.popleft() if que else -1)
    elif order == "size":
        print(len(que))
    elif order == "empty":
        print(1 if not que else 0)
    elif order == "front":
        print(que[0] if que else -1)
    elif order == "back":
        print(que[-1] if que else -1)