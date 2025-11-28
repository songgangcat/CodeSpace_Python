from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
deq = deque()

for _ in range(N):
    order, *rest = map(int, input().split())
    if order == 1:
        deq.appendleft(rest[0])        
    elif order == 2:
        deq.append(rest[0])
    elif order == 3:
        print(deq.popleft() if deq else -1)
    elif order == 4:
        print(deq.pop() if deq else -1)
    elif order == 5:
        print(len(deq))
    elif order == 6:
        print(1 if not deq else 0)
    elif order == 7:
        print(deq[0] if deq else -1)
    elif order == 8:
        print(deq[-1] if deq else -1)