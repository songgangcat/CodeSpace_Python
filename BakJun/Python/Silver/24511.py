from collections import deque
import sys
input = sys.stdin.readline

#큐= 왼빼우넣
#스택 = 우빼우넣
result = []

N = int(input()) #자료구조 개수
A = deque(map(int, input().split())) #que or stk 판별
B = deque(map(int, input().split())) #자료구조 원소
M = int(input()) # 삽입 수열 길이
C = deque(map(int, input().split())) #삽입 원소

for _ in range(N):
    if A.popleft() == 0:
        B.rotate(-1)
    else:
        B.popleft()

for x in C:
    B.appendleft(x)
    result.append(B.pop())

print(*result)