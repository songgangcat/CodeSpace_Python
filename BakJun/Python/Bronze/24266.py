import sys

n = int(sys.stdin.readline().rstrip())

print(n**3)
print(3)

#T(n) = n**3 + 1
#T'(n) = n**3
#O(n**3)