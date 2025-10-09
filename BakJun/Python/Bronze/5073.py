#Equilateral :  세 변의 길이가 모두 같은 경우
#Isosceles : 두 변의 길이만 같은 경우
#Scalene : 세 변의 길이가 모두 다른 경우
#단 주어진 세 변의 길이가 삼각형의 조건을 만족하지 못하는 경우에는 "Invalid" 를 출력한다. 예를 들어 6, 3, 2가 이 경우에 해당한다. 가장 긴 변의 길이보다 나머지 두 변의 길이의 합이 길지 않으면 삼각형의 조건을 만족하지 못한다.
#각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력된다. 마지막 줄은 0 0 0이며 이 줄은 계산하지 않는다.
#각 입력에 맞는 결과 (Equilateral, Isosceles, Scalene, Invalid) 를 출력하시오.


while True:
    a, b, c = map(int, input().split())
    sides = sorted([a, b, c])
    if a == 0 and b == 0 and c == 0:
        break
    elif sides[2] >= sides[0] + sides[1]:
        print("Invalid")
    elif a == b == c:
        print("Equilateral")
    elif a == b or b == c or a == c:
        print("Isosceles")
    else:
        print("Scalene")