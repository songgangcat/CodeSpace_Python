import math

def nPr(n, r):
    if r > n or r < 0:
        return 0
    return math.factorial(n) // math.factorial(n - r)

N = int(input())
print(nPr(N, 2))