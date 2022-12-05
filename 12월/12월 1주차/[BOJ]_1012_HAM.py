import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
T = int(input())

def search(x,y):
    if x < 0 or x >= M or y < 0 or y >= N:
        return

    if graph[x][y] == 0:
        return


    graph[x][y] = 0 # 탐색한 배추는 0으로 갱신

    # 동서남북 탐색
    search(x+1,y)
    search(x,y+1)
    search(x-1,y)
    search(x,y-1)


for _ in range(T):
    N, M, K = map(int, input().split()) # 가로길이, 세로길이, 배추 수
    graph = [[0] * N for _ in range(M)]

    result = 0 # 지렁이 수

    # 그래프 생성
    for _ in range(K): # 배추 수 만큼 반복
        a,b = map(int,input().split())
        graph[b][a] = 1 # 배추 위치 표기

    # dfs
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1: # 배추가 존재하는 경우
                search(i,j) # 인접 배추 탐색
                result += 1 # search가 종료하면, 지렁이 수 추가

    print(result)