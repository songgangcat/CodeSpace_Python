#정석 O(1)
import sys
input = sys.stdin.readline

N = int(input())
count = 0

used_col = [False] * N              # 열 점유, used_col[c] == True면 열 점유됨
used_diag1 = [False] * (2 * N - 1)  # (row + col)값이 같으면 "/" 방향 대각선
used_diag2 = [False] * (2 * N - 1)  # (row - col) 값이 같으면 "\" 방향 대각선, 음수 방지용 +(N-1)

def queen(row):
    global count
    if row == N:
        count += 1
        return

    for col in range(N): 
        d1 = row + col 
        d2 = row - col + (N - 1) 

        if used_col[col] or used_diag1[d1] or used_diag2[d2]:
            continue

        used_col[col] = True
        used_diag1[d1] = True
        used_diag2[d2] = True

        queen(row + 1)

        used_col[col] = False #행 하나 뒤로 가면서 하나 원상복구
        used_diag1[d1] = False
        used_diag2[d2] = False

queen(0)
print(count)



#아래는 스스로 만든 코드, 맞지만 시간 초과뜸
import sys
input = sys.stdin.readline

col = [] #요소는 열 번호, 인덱스+1은 행 번호
count = 0

def queen(row):
    global count
    if row == N:
        count += 1 #경우의 수 하나 완성, 초기화 후 0으로 재귀
        return
    
    for i in range(N): #row+1행에서 열 하나씩 돌리기
        if col and i in col: #같은 열에 있으면 제외하고 다음 열 
            continue
        
        ok = True   #기본값 True, 마지막 "대각선이면 if문"이 밖에 있음으로 얘도 밖에 두기 

        for prev_row in range(row): #col이전 요소들이랑 하나씩 비교, 하나라도 대각선이면 break
            if abs(i - col[prev_row]) == row - prev_row: #행 차이 == 열 차이면
                ok = False 
                break #대각선 검사 for문 깨고 break, 대각선 검사 멈춤
            
        if not ok: #대각선이면
            continue #이번 열 버리고 다음열

        col.append(i) #col에 열 번호 추가
        queen(row + 1) #다음 행 재귀 -> row == N일때 끝나면서 pop으로 이어짐, 이전 열 이어서 순환
        col.pop() #얘가 있어야 돌아갈때 문제 안생김  


N = int(input())
queen(0)
print(count)
