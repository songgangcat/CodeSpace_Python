import sys
from math import gcd
from functools import reduce

input = sys.stdin.readline

N = int(input())
nums = []
diff = []

for _ in range(N):
    num = int(input())
    nums.append(num)
    if len(nums) >= 2:
        diff.append(nums[-1] - nums[-2])

g = reduce(gcd, diff)
length = nums[-1] - nums[0]
total_trees = length // g + 1

print(total_trees - N)
