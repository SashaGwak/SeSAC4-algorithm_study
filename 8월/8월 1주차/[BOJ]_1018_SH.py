# 체스판 다시 칠하기(1018)
import sys
N, M = map(int, input().split())
chess = [] # 체스판
count = [] # 수정해야할 출력값 저장할 리스트 

for _ in range(N):
    chess.append(sys.stdin.readline())

for a in range(N - 7): # 8*8 으로 검사해야할 영역 지정
    for b in range(M -7): 
        index1 = 0 # W 으로 시작할 경우 count
        index2 = 0 # B로 시작할 경우 count
        for i in range(a, a + 8): # 8*8 검사 시작
            for j in range(b, b + 8):
                if (i + j) % 2 == 0:
                    if chess[i][j] != 'W':
                        index1 += 1
                    if chess[i][j] != 'B': 
                        index2 += 2
                else: 
                    if chess[i][j] != 'B':
                        index1 += 1 
                    if chess[i][j] != 'W':
                        index2 += 1
        count.append(min(index1, index2))

print(min(count)) # 리스트 형태 말고 값으로 나오기 위해 