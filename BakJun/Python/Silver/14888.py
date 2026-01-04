import sys
input = sys.stdin.readline

#N개로 이루어진 수열
#N-1개의 사칙연산자
#주어진 수 순서 고정, 연산자 랜덤
#계산 -> 연산자 우선순위 무시, 앞에서부터 진행 
#=> 변수 만들고 하나씩 계산해야 할듯
#나눗셈은 정수 나눗셈, 몫만 취함
#음수를 양수로 나눌 때 => 양수로 바꾼 뒤, 몫을 취하고 음수로 바꿈
#결과 최대와 최소를 구하기

#함수 안에 for문 이용해서 하나씩 ops에서 꺼내서 넣고, result에 넣기 반복, 마무리되면 끝
#그럼 함수 변수는 아마 깊이가 될거고, 종료는 연산자 N-1개를 전부 사용했을 때

N = int(input())
nums = list(map(int, input().split()))
ops = list(map(int, input().split())) #인덱스로 각각 남은 개수 관리
result = [] #최종 cur값 모아서, 마지막에 max, min 정리할 예정


#계산을 편하게 위해 보조함수 apply 선언
def apply(op, a, b): #각각 ops 인덱스, 변수 1, 변수 2
    if op == 0: #+
        return a+b
    if op == 1: #-
        return a-b
    if op == 2: #*
        return a*b
    if op == 3: #/
        if a<0:
            return - (abs(a)//b)
        return a//b




#cur을 함수 인자로 사용해야, 각 계산이 독립적으로 작용하기
def dfs(idx, cur): # idx == 깊이 == 연산하고 있는 숫자의 인덱스, cur == nums[0] (기본값)
    if idx == N-1: #연산자 모두 소진하면 결과값 result에 저장
        result.append(cur)
        return
    
    for i in range(4):
        if ops[i] == 0: #이미 다 사용했으면 pass
            continue
        
        ops[i] -= 1 #해당 연산자 값 줄이기
        nxt = apply(i, cur, nums[idx+1]) #보조함수 이용, 다음 함수 계산
        dfs(idx+1, nxt) #더 깊은 함수 재귀
        ops[i] += 1 #ops 값 복구

dfs(0, nums[0])
print(max(result))
print(min(result))
#재귀 끝나면 cur, ops 복구하는 과정 넣기