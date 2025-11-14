import sys
input = sys.stdin.readline

result = []

N = int(input())
num = list(map(int, input().split()))
count = {}
for x in num:
    count[x] = count.get(x, 0) + 1

M = int(input())
queries = list(map(int, input().split()))
for x in queries:
    result.append(count.get(x, 0))

print(*result)