import sys
input = sys.stdin.readline

def han(n, start, mid, end):
    if n == 1:
        print(start, end)
        return
    
    han(n-1, start, end, mid)
    print(start, end)
    han(n-1, mid, start, end)    


N = int(input())
print((1 << N)-1)
han(N, 1, 2, 3)
