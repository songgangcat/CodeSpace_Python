import sys
input = sys.stdin.readline

cnt = 0 

def recursion(s, l, r):
    global cnt
    cnt += 1

    if l >= r:
        return 1
    if s[l] != s[r]:
        return 0
    return recursion(s, l+1, r-1)

def isPalindrome(s):
    global cnt
    cnt = 0
    return recursion(s, 0, len(s) - 1)

N = int(input())
for _ in range(N):
    S = input().rstrip()
    print(isPalindrome(S), cnt)
