#회원들을 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서로 정렬하는 프로그램을 작성하시오.

import sys
input = sys.stdin.readline

N = int(input().rstrip())

lst = [input().rstrip().split() for _ in range(N)]
lst.sort(key=lambda x: int(x[0]))
result = [' '.join(x) for x in lst]

print('\n'.join(result))