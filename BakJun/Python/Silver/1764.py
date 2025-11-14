import sys
input = sys.stdin.readline

no = []
nod = {}
result = []

N, M = map(int, input().split())
for _ in range(N):
    no.append(input().rstrip())
for _ in range(M):
    no.append(input().rstrip())

for x in no:
    nod[x] = nod.get(x, 0) + 1

result = [x for x, y in nod.items() if y == 2]

print(len(result))
print('\n'.join(sorted(result)))