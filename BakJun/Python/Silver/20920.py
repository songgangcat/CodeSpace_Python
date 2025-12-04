import sys
from collections import Counter
input = sys.stdin.readline

N, M = map(int, input().split())

words = []
for _ in range(N):
    w = input().rstrip()
    if len(w) >= M:        # M 이하 단어 소거
        words.append(w)

cnt = Counter(words)

# (단어, 빈도) 리스트 생성 후 정렬
# key = (-빈도, -길이, 사전순)
result = sorted(cnt.items(), key=lambda x: (-x[1], -len(x[0]), x[0]))

# 단어만 출력
print('\n'.join(word for word, _ in result))
