#10진법 수 N이 주어진다. 이 수를 B진법으로 바꿔 출력하는 프로그램을 작성하시오.
#첫째 줄에 10진법 수 N을 B진법으로 출력한다.

N, B = map(int, input().split())
digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
result = ''

while N > 0:
    result = digits[N % B] + result #나머지를 문자화해서 result 가장 앞쪽에 붙임/
    N //= B # N을 B로 나눈 몫을 N에 주입, 반복

print(result)
