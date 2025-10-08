#

N = int(input())

layer = 1  # 층 (시작은 1)
end = 1    # 각 층의 마지막 방 번호

while N > end:
    end += 6 * layer  # 다음 층의 마지막 방 번호
    layer += 1        # 층 수 증가

print(layer)
