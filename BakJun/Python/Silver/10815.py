import sys
input = sys.stdin.readline

N = int(input())
card = set(map(int, input().split()))
M = int(input()) 
lst = list(map(int, input().split()))
result = []

for x in lst:
    if x in card:
        result.append(1)
    else:
        result.append(0)

print(*result)