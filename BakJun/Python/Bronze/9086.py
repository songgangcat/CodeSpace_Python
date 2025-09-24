#문자열을 입력으로 주면 문자열의 첫 글자와 마지막 글자를 출력하는 프로그램을 작성하시오.
#입력의 첫 줄에는 테스트 케이스의 개수 T(1 ≤ T ≤ 10)가 주어진다. 각 테스트 케이스는 한 줄에 하나의 문자열이 주어진다. 문자열은 알파벳 A~Z 대문자로 이루어지며 알파벳 사이에 공백은 없으며 문자열의 길이는 1000보다 작다.
#각 테스트 케이스에 대해서 주어진 문자열의 첫 글자와 마지막 글자를 연속하여 출력한다.

T = int(input())  # 테스트 케이스 개수 입력받기
list_a = []  # 문자열을 저장할 리스트

# 각 테스트 케이스마다 첫 문자와 마지막 문자만 저장
for i in range(T):
    S = input()
    list_a.append(S[0] + S[-1])  # 첫 문자와 마지막 문자만 결합하여 저장

# 각 결과를 한 줄씩 출력
for result in list_a:
    print(result)

    
##for result in list_a:
#     print(result)
#⇒ 리스트 안에 요소 하나씩 순서대로 출력 가능!

#join 활용법: separator.join(iterable)
#separator: 요소들 사이에 삽입될 문자열(”,” / “\n” 등)
#iterable: 연결할 문자열들이 포함된 반복가능객체(리스트, 문자열등)
#separator가 iterable 요소들 사이에 들어가서 연결됨.
#ex) print(”\n”.join(list_a)) → list 내 요소들을 줄바꿈해서 출력