from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
moves = list(map(int, input().split()))
deq = deque((i, num) for i, num in enumerate(moves, start= 1))
result = []

idx, x = deq.popleft()
result.append(idx)
while deq:
    if x>0:
        for _ in range(x-1):
            deq.append(deq.popleft())
    
    else:
        for _ in range(-x):
            deq.appendleft(deq.pop())
    idx, x = deq.popleft()
    result.append(idx)

print(*result)



#정석답변 -> 이해하기

from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
moves = list(map(int, input().split()))

# (풍선 번호, 이동값)
deq = deque((i + 1, moves[i]) for i in range(N))
result = []

# 풍선이 남아 있는 동안 반복
while deq:
    idx, move = deq.popleft()  # 맨 앞 풍선 터뜨리기
    result.append(idx)         # 번호 기록

    if not deq:                # 더 남은 풍선 없으면 종료
        break

    if move > 0:
        # 이미 한 칸(popleft) 움직였으니까 move-1만큼 왼쪽 회전
        deq.rotate(-(move - 1))
    else:
        # 음수는 그대로 오른쪽으로 -move만큼 회전
        deq.rotate(-move)

print(*result)
