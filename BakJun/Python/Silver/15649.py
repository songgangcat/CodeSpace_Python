import sys
input = sys.stdin.readline


def backtrack(depth):
    if depth == M:
        print(*path)
        return
    
    for i in range(1, N+1):
        if i in path: #중복일 시 넘어감
            continue
        path.append(i) #추가
        backtrack(depth + 1) #깊이 + 1, 이 함수가 다 끝나야 아래 줄이 실행됨
        path.pop() # 뒤로 돌아가기

path = []

N, M = map(int, input().split())
backtrack(0)


