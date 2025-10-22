import sys

n = int(sys.stdin.readline().rstrip())

print(n*(n-1)//2)
print(2)

#T(n) = n*(n-1)/2 + 1
#T'(n) = n*(n-1)/2
#O(n**2)