def dfs(y,x):
    # 범위 벗어나는 경우 건너뛰기
    if x < 0 or x >= w or y < 0 or y >= h:
        return False
    # 바다인경우 건너뛰기
    # if graph[x][y]==0:
    #     return False

    # 섬인경우 재귀
    if graph[y][x] == 1:
        #방문처리
        graph[y][x] = 0
        # 상하좌우 탐색
        dfs(y,x-1)
        dfs(y,x+1)
        dfs(y-1,x)
        dfs(y+1,x)
        # 대각선 탐색
        dfs(y-1,x-1)
        dfs(y-1,x+1)
        dfs(y+1,x-1)
        dfs(y+1,x+1)
        return True
    return False


while True:
    w,h = map(int,input().split())

    if w == 0 & h ==0 :
        break

    graph = []
    for _ in range(h):
        graph.append(list(map(int,input().split())))

    result = 0
    for i in range(h):
        for j in range(w):
            if dfs(i,j) == True:
                result += 1
    print(result)