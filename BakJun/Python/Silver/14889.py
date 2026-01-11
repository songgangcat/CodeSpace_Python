import sys
input = sys.stdin.readline

#불리언 이용해서 for문에서 true로 표기, if xx: 이용해서 true/false 각 팀에 모으기

N = int(input())
table = [list(map(int, input().split())) for _ in range(N)] # 표 받기

ans = float("inf") #최솟값 넣어두는 변수 => 함수 안에서 마지막에 항상 최신화
selected = [False]*N #False N개 리스트 => 인덱스로 팀에 선택되었는지 확인하는 용도


#팀 조합 만드는 함수 dfs() 
def dfs(idx, cnt): #idx == 현재 고려하고 있는 첫번째 팀원 / cnt == 팀원 명수
    global ans
    if ans == 0: #0보단 작을 수 없으니 컷
        return

    if cnt == N//2: #팀이 다 짜지면
        A, B = [], [] #리스트 두개 만들어두고
        for i in range(N):
            (A if selected[i] else B).append(i) #selected[i]가 True면 A로 추가, 아니면 B
        
        diff = abs(calc(A)-calc(B)) #A팀과 B팀의 능력치 합의 절댓값
        ans = min(diff, ans) #ans와 현재 diff 비교 -> ans 최신화

        return #이전 함수로 복귀
    
    #하나씩 고르고 백트래킹하는 함수
    for i in range(idx, N): #idx~인원수에서 돌리기 -> idx부터 시작해야 중복 조합 안나옴 
        selected[i] = True
        dfs(i+1, cnt+1)
        selected[i] = False


#계산 함수 calc()
def calc(team):
    score = 0
    for i in range(len(team)):
        for j in range(i + 1, len(team)): # i < j 인 경우만 계산 -> 중복, 자기 자신 제거
            a = team[i]
            b = team[j]
            score += table[a][b] + table[b][a]
    
    return score

#A팀이 더 높든 B팀이 더 높든 상관 x ==> 0번(1번선수)를 A팀에 박아두고 시작하자!
# ==> 뒤집힌 중복 소거하고 1/2만 탐색
selected[0] = True #0번(1번선수) A팀에 고정해서 1/2 탐색하기
dfs(1, 1) #0번(1번선수)가 A팀이기 때문에 1번(2번선수)부터 탐색, cnt(팀원 명수) 1로 시작
print(ans)