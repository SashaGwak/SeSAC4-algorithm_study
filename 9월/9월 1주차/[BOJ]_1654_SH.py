# 랜선 자르기(1654)
import sys 
# K 이미 가지고 있는 랜선의 개수, N 필요한 랜선의 개수 
K, N = map(int, sys.stdin.readline().split())
# 가지고 있는 K 랜선의 길이 입력받기 
lan = [int(sys.stdin.readline()) for _ in range(K)]

# 이분 탐색 시작 
start, end = 1, max(lan)

while start <= end: 
    mid = (start + end) // 2
    lines = 0 # 랜선 수 
    for i in lan: 
        lines += i // mid  # 잘린 랜선 수 

    if lines >= N: # 최장 랜선길이를 찾아야하므로 start점 바꿔줌 
        start = mid + 1
    else: 
        end = mid - 1

print(end)