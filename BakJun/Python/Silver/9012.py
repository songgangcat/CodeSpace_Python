import sys
input = sys.stdin.readline


T = int(input())
for _ in range(T):
    stack = []
    for x in input().rstrip():
        if x == '(':
            stack.append('(')
        elif x == ')':
            if not stack:
                print("NO")
                break
            else:
                stack.pop()
    else:
        print("NO" if stack else "YES")
