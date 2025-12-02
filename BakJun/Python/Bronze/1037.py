import sys
input = sys.stdin.readline

long = int(input())
nums = list(map(int, input().split()))

print(max(nums)*min(nums))