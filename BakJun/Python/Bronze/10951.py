#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#입력은 여러 개의 테스트 케이스로 이루어져 있다.
#각 테스트 케이스는 한 줄로 이루어져 있으며, 각 줄에 A와 B가 주어진다. (0 < A, B < 10)
#각 테스트 케이스마다 A+B를 출력한다.


#<gpt 1>
while True:
    try:
        a, b = map(int, input().split())
        print(a+b)
    except EOFError:
        break
#try:
#    *실행할 코드 (에러가 날 수도 있음)
#except 에러종류:
#    에러카 발생했을 때 실행할 코드
#else:
#    에러가 안 났을 때 실행할 코드
#finally:
#    에러 발생 여부와 상관 x 무조건 실행할 코드
#*try 혼자 쓸수는 x


#<gpt 2>
#import sys

#for line in sys.stdin:
#    a, b = map(int, line.split())
#    print(a + b)

#for line in sys.stdin: ==> 모든 시스템 표준 입력을 줄별로 읽어라 = 입력 끝나면 자동으로 종료
#     ** data = sys.stdin.read()하면 전체 읽고,
#        char = sys.stdin.read(1)하면 한 글자 읽음
#line.split() => 문자열 line을 공백(스페이스, 탭, 줄바꿈 등) 기준으로 잘라서 리스트로 반환

#sys 모듈에는 3가지 기본 스크림 있음
#1. sys.stdin (표준 입력) 
#   -> 기본적으로 키보드와 연결, 프로그램이 외부에서 데이터 받아들이는 통로, input() -> sys.stdin.readline() 활용함
#2. sys.stdout (표준 출력) 
#   -> 기본적으로 터미널 화면과 연결, 프로그램이 외부로 결과를 내보내는 통로, print() -> sys.stdout.write() 활용함
#3. sys.stderr (표준 에러)
#   -> 기본적으로 화면에 출력되지만, stdout과 분리 -> 로그 관리에 사용, 에러 메세지를 출력하는 전용 통로