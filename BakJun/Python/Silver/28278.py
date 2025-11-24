import sys
input = sys.stdin.readline


N = int(input())
stack = []

for i in range(N):
    cmd, *rest = map(int, input().split())
    if cmd == 1:
        stack.append(rest[0])
    elif cmd == 2:
        print(-1 if not stack else stack.pop())
    elif cmd == 3:
        print(len(stack))
    elif cmd == 4:
        print(1 if not stack else 0)
    elif cmd == 5:
        print(-1 if not stack else stack[-1])
    