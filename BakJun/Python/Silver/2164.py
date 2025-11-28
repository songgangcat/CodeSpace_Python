from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
que = deque(range(1, N+1))

while len(que) > 1:
    que.popleft()
    que.append(que.popleft())

print(que[0])
