# 11403 경로 찾기

import sys

N = int(sys.stdin.readline()) # 정점의 개수
G = [list(map(int, sys.stdin.readline().split())) for _ in range(N)] # 그래프의 인접 행렬

def dfs(v):
    for i in range(N):
        if C[i] == 0 and G[v][i] == 1: # 방문하지 않고 간선이 존재하면
            C[i] = 1 # 1을 표시
            dfs(i)

for i in range(N):
    C = [0 for _ in range(N)] # 방문
    dfs(i)
    print(*C) # 리스트의 경우 : '*' 기호를 넣어서 각각의 값을 출력할 수 있음