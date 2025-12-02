import sys
input = sys.stdin.readline

N = int(input())
dance = {"ChongChong"}

for _ in range(N):
    A, B = map(str, input().split())
    if A in dance or B in dance:
        dance.add(A)
        dance.add(B)

print(len(dance))