import sys
input = sys.stdin.readline

while True:
    stack = []
    S = input().rstrip()
    if S == ".":
        break
    for x in S:
        if x in "[(":
           stack.append(x)
        elif x == "]":
            if not stack or stack[-1] != "[":
                print("no")
                break
            else:
                stack.pop()
        elif x == ")":
            if not stack or stack[-1] != "(":
                print("no")
                break
            else:
                stack.pop()
    else:
        print("yes" if not stack else "no")
