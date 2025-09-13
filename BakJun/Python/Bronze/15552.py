# for문 문제를 풀기 전에 주의해야 할 점이 있다. 입출력 방식이 느리면 여러 줄을 입력받거나 출력할 때 시간초과가 날 수 있다는 점이다.
#Python을 사용하고 있다면, input 대신 sys.stdin.readline을 사용할 수 있다. 
# 단, 이때는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가로 해 주는 것이 좋다.
#또한 입력과 출력 스트림은 별개이므로, 테스트케이스를 전부 입력받아서 저장한 뒤 전부 출력할 필요는 없다. 테스트케이스를 하나 받은 뒤 하나 출력해도 된다.
#첫 줄에 테스트케이스의 개수 T가 주어진다. T는 최대 1,000,000이다. 다음 T줄에는 각각 두 정수 A와 B가 주어진다. A와 B는 1 이상, 1,000 이하이다.

import sys
input = sys.stdin.readline
write = sys.stdout.write

T = int(input())
for _ in range(T):
    a, b = map(int, input().split())
    write(str(a + b) + '\n')

# import sys -> 파이썬의 표준 라이브러리 sys 모듈 불러옴

#input = sys.stdin.readline
#input() 함수 대신, sys.stdin.readline()을 사용하겠다는 의미
#sys.stdin.readline(): 문자열 한 줄 전체를 입력으로 읽어옴
#끝에 \n(줄바꿈 문자)이 포함되어서 읽힘 => 필요시 .strip()으로 제거 (여기선 .split()이라서 ㄱㅊ)

#write = sys.stdout.write
#print() 대신, sys.stdout.write()이 사용됨
#sys.stdout.write() 특징: 문자열만 출력 가능 (숫자는 str()로 변환 필요)
#자동 줄바꿈 X => '\n' 직접 붙여야 줄 바뀜
#반복문에서 많은 출력을 할때 print()보다 빠름