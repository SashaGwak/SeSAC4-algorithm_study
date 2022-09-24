# 연결 요소의 개수(11724)
import sys
input = sys.stdin.readline

# N 정점의 개수, M 간선의 개수
N, M = map(int, input().split())

graph = [[] for _ in range(N+1)]
