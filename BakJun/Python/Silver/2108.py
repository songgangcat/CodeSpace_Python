import sys
from collections import Counter
input = sys.stdin.readline

N = int(input())
nums = [int(input()) for _ in range(N)]
nums.sort()

cnt = Counter(nums)
mc = cnt.most_common()

if len(mc) > 1 and mc[0][1] == mc[1][1]:
    mode = mc[1][0]
else:
    mode = mc[0][0]

print(round(sum(nums)/N))         # 산술평균 (2108은 반올림 필요)
print(nums[N//2])                 # 중앙값
print(mode)                       # 최빈값
print(nums[-1] - nums[0])         # 범위
