# 이진탐색을 통해 막대과자의 길이를 구해 출력한다.
import sys
input = sys.stdin.readline
m, n = map(int, input().split())
L = list(map(int, input().split()))
start = 1
end = int(1e9) #1e9 = 1*109 = 1000000000
result = 0
while start <= end:
    mid = (start + end) // 2
    countOfSnack = 0
    for l in L:
        countOfSnack += l // mid
    if countOfSnack >= m:
        result = max(result, mid)
        start = mid + 1
    else:
        end = mid - 1
print(result)