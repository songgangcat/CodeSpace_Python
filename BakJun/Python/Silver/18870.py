#좌표 압축

import sys
input = sys.stdin.readline

N = int(input())
X = list(map(int, input().split()))

uniq = sorted(set(X))
rank = {v: i for i, v in enumerate(uniq)}

print(*[rank[x] for x in X])
