# 9465(스티커)
import sys
input = sys.stdin.readline

for test in range(int(input())):
    n = int(input())
    arr = [[0]*100000,[0]*100000]

    # 스티커 점수 값 받은 리스트
    for idx, value in enumerate(map(int,input().split())):
        # enumerate(리스트) -> 인덱스 번호와 컬렉션의 원소를 tuple 형태로 반환 
        # (0, 50)(1, 10)... 이런식으로 
        # 여기서는 tuple 형태 변환이용하여 인덱스와 값 받아준 것 
        arr[0][idx] = value
    for idx, value in enumerate(map(int,input().split())):
        arr[1][idx] = value

    # 미리 비교위하여 [i][1] 자리 값 더해놓기
    arr[0][1] += arr[1][0] # 맨아래쪽부터 바로 오른쪽 대각선 시작하는라인 arr[0]
    arr[1][1] += arr[0][0] # 맨위부터 바로 오른쪽 대각선  arr[1]

    for i in range(2, n):
        arr[0][i] += max(arr[1][i-1], arr[1][i-2])
        # 한 칸 앞에 애, 두칸 앞에 애 중 큰애가 더해짐
        arr[1][i] += max(arr[0][i-1], arr[0][i-2])

    print(max(arr[0][n-1], arr[1][n-1]))