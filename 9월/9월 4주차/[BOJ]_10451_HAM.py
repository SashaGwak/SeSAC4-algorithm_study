from sys import stdin
input = stdin.readline

# 재귀로 현 숫자가 가리키는 다음 숫자 확인
def dfs(startNum, originNum):
    global cycle
    nextNum = A[startNum]   # 현 숫자가 가리키는 다음 숫자
    if check[nextNum]:      # 이미 방문했다면 사이클 이루는지 확인
        if nextNum == originNum:    
            cycle += 1      # 사이클 이룬 것이므로 +1
            return
    else:   				# 첫 방문이라면 방문 표시
        check[nextNum] = 1
        dfs(nextNum, originNum)     # 재귀로 다음 숫자 확인

# main
T = int(input())
for _ in range(T):
    N = int(input())
    A = [0] + list(map(int, input().split()))
    cycle = 0
    check = [0] * (N+1)             # 방문 표시
    for start in range(1, N+1):
        if check[start]:            # 이미 방문한 곳이면 탐색 X
            continue
        check[start] = 1            # 새로 탐색 시작
        dfs(start, start)           # 이동할 숫자와 사이클 확인용 시작한 숫자

    print(cycle)