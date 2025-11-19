import sys
input = sys.stdin.readline

S = input().rstrip()
result = set()


for j in range(len(S)):
    for i in range(len(S)-j):
	    result.add(S[j:j+i+1])

print(len(result))
