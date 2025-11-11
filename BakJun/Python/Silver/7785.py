
import sys
input = sys.stdin.readline
S = set()

n = int(input())
for i in range(n):
    name, ent = map(str, input().split())
    if ent == 'enter':
        S.add(name)
    else:
        S.remove(name)

result = sorted(list(S), reverse=True)
print('\n'.join(result))