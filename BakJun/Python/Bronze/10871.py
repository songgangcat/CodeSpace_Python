#정수 N개로 이루어진 수열 A와 정수 X가 주어진다. 이때, A에서 X보다 작은 수를 모두 출력하는 프로그램을 작성하시오.
#첫째 줄에 N과 X가 주어진다. (1 ≤ N, X ≤ 10,000)
#둘째 줄에 수열 A를 이루는 정수 N개가 주어진다. 주어지는 정수는 모두 1보다 크거나 같고, 10,000보다 작거나 같은 정수이다.
#X보다 작은 수를 입력받은 순서대로 공백으로 구분해 출력한다. X보다 작은 수는 적어도 하나 존재한다.

N, x = map(int, input().split())
list_a = list(map(int, input().split()))

list_b = []
for i in range(N):
    if list_a[i] < x:
        list_b.append(list_a[i])

print(*list_b)


#리스트에 x를 추가할때는 .append(x) 활용
#리스트로 출력 하는게 아닌, 공백 구분으로 출력하려면 print(*list_b)


#<GPT 1> - 리스트 컴프리헨션 => pythonic!

#N, x = map(int, input().split())
#list_a = list(map(int, input().split()))#

#list_b = [a for a in list_a if a < x]

#print(*list_b)

#리스트 컴프리헨션: list_a = [표현식 for 변수 in 반복가능객체 if 조건식]
# - `for 변수 in 반복가능객체` : 기존 리스트, range, 문자열 같은 반복 가능한 자료를 순회
# - `if 조건식` : 특정 조건을 만족하는 원소만 필터링
# - `표현식` : 조건을 만족했을 때 리스트에 넣을 값

#<GPT 2> - filter 함수 버전

#N, x = map(int, input().split())
#list_a = list(map(int, input().split()))

#list_b = list(filter(lambda a: a < x, list_a))

#print(*list_b)

##filter: filter(함수, 반복가능객체(iterable))
#반복가능개체 = 리스트, 튜플, 문자열 등
#함수 = 각 원소를 입력으로 받아 True/False를 반환해야 함
#True → 해당 원소 유지
#False → 해당 원소 제외
#*반환 값은 filter 객체이므로, 결과를 리스트로 보려면 리스트로 변환해주는 list() 감싸기

#lambda 함수 : 익명함수. def 키워드로 함수를 만들지 않고, 한 줄로 간단히 정의할 수 있는 함수. 
#:lambda 매개변수: 표현식
#매개변수 = 함수에 전달되는 값
#표현식 =  실행할 코드(반드시 결과값 반환)
#return 키워드 쓰지 x(자동으로 반환)
#*일반 함수
# def add(a, b):
#      return a + b

#*lambda 함수
#add = lambda a, b: a + b
#print(add(3, 5))
