# 팀 프로젝트(9466)
# 반드시 team의 마지막 학생은 team의 첫 학생을 지목해야 팀이 된당 
import sys
sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

K = int(input()) # test 수

def dfs(v):
    global result
    visited[v] = 1 # 방문한 정점 기록
    traced.append(v) # 탐색 경로 저장

    w = graph[v] # 다음 방문할 정점
    if visited[w] == 1: # 방문 가능한 곳이 끝났는지 체크
        if w in traced: # 탐색 경로에 다음 방문할 정점이 존재하면 순환
            result += traced[traced.index(w):] # 사이클이 되는 구간부터만 팀을 이룸
        return
    else:
        # 방문하지 않은 곳이면 
        dfs(w) # 탐색 진행



for _ in range(K):
    V = int(input()) # 학생 수
    graph = [0] + list(map(int, input().split())) # 그래프 생성, 맨 앞에 [0]을 추가해 인덱스에 접근하기 편리하도록.
    visited = [0] * (V+1) # 방문한 정점를 담을 stack 생성
    result = [] # 팀을 구성한 학생 수


    for i in range(1, V+1): # 1번 학생부터 탐색 시작.
        if visited[i] == 0: # 방문한 정점이 아닌 경우에만 탐색 진행
            traced = [] # 탐색 경로 정보를 담을 stack 생성
            dfs(i)

    print(V - len(result))