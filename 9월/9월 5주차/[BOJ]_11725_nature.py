# 11725 트리의 부모 찾기

import sys
sys.setrecursionlimit(10**9)

input = sys.stdin.readline
N = int(input()) # 노드의 개수

graph = [[] for _ in range(N+1)] # 트리

for i in range(N-1): # 트리 구조 입력
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

def find(x):
    if graph[x]: # 자식 노드가 있을 때 
        for child in graph[x]: # 자식에 대해 
            result[child] = x # data의 부모는 x
            graph[child].remove(x) # graph[data]에서 부모 x 삭제
            find(child)

# 1번 노드부터 탐색 시작
# 1번 노드 => 루트 노드
# 따라서 graph[1]에는 자식 노드만 있음
# graph[1] 안에 있는 child에 대해 result[child]를 1로 지정하고
# graph[child]에서 1을 제거
# 그러면 graph[child]에는 자식 노드들만 남게 됨

result = [0] * (N+1)

find(1)

for i in range(2, N+1):
    print(result[i])