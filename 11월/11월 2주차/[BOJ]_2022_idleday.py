# 2022 사다리
# 이분탐색

def get_c(x, y, width):
    h1 = (x**2 - width**2)**0.5
    h2 = (y**2 - width**2)**0.5
    c = h1 * h2 / (h1 + h2)
    return c


def binarySearch():
    x, y, c = map(float, input().split())
    start, end = 0, min(x, y)   # end를 둘 중 작은 값으로 설정
    res = 0

    while (end - start) > 0.000001:
        width = (start + end) / 2
        res = width
        # 기존의 c보다 같거나 크면 w값을 키워 h1, h2의 값을 작게 해주기
        if get_c(x, y, width) >= c:
            start = width
        else:
            end = width
    print(res)


binarySearch()
