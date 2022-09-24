# 연결 요소의 개수(11724)
import sys
input = sys.stdin.readline

# N 정점의 개수, M 간선의 개수
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]

for i in range(M): 
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(1, N+1): 
    graph[i].sort()
'''
6 5
1 2
2 5
5 1
3 4
4 6
일 경우, 그래프 [[], [2, 5], [1, 5], [4], [3, 6], [1, 2], [4]]
'''

