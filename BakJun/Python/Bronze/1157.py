#알파벳 대소문자로 된 단어가 주어지면, 이 단어에서 가장 많이 사용된 알파벳이 무엇인지 알아내는 프로그램을 작성하시오. 단, 대문자와 소문자를 구분하지 않는다.
#첫째 줄에 알파벳 대소문자로 이루어진 단어가 주어진다. 주어지는 단어의 길이는 1,000,000을 넘지 않는다.
#첫째 줄에 이 단어에서 가장 많이 사용된 알파벳을 대문자로 출력한다. 단, 가장 많이 사용된 알파벳이 여러 개 존재하는 경우에는 ?를 출력한다.


S = input().strip().lower()
list_a = []

for i in range(97,123):
    list_a.append(S.count(chr(i)))

if list_a.count(max(list_a)) >= 2:
    print("?")
else:
    print(chr(list_a.index(max(list_a))+97).upper())

#<GPT>
#S = input().strip().upper()
#cnt = [S.count(chr(i)) for i in range(65,91)]

#if cnt.count(max(cnt)) > 1:
#    print("?")
#else:
#    print(chr(cnt.index(max(cnt))+65).upper())
