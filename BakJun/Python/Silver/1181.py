#알파벳 소문자로 이루어진 N개의 단어가 들어오면 아래와 같은 조건에 따라 정렬하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

n = int(input())
words = {input().strip() for _ in range(n)} 

for w in sorted(words, key=lambda x: (len(x), x)):
    print(w)
