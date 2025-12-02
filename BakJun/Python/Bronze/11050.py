import math

def nCr(n, r):
    if r < 0 or r > n:
        return 0
    r = min(r, n - r) 
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

N, K = map(int, input().split())
print(nCr(N, K))