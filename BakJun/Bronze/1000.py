a, b = map(int, input().split()) 
print(a+b)
# map = 리스트 요소마다 함수 적용 map(함수, 리스트)
# + map 그 자체로는 print 불가능. list(.split() 활용 가능)나 반복문을 통해 뽑아내야 함
# .split() => 띄어쓰기를 기준으로 각각을 묶어 리스트화 *단 이걸 고지를 안해주면 활용 방식 어려움

# a,b = (int(input()),int(input()))
# print(a+b)
# 도 가능함