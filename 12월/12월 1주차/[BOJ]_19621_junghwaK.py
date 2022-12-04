import sys
sys.setrecursionlimit(3000000)

def dfs(node, t):
    t += li[node][2]
    if li[node][1] > max_s:
        res.append(t)        
    for n in range(node+1, N):
        if li[node][1] > li[n][0]:
            continue
        dfs(n, t)

N = int(input())
li = [list(map(int, input().split())) for _ in range(N)]
li.sort(key=lambda x:(x[0], x[1]))
res = []
max_s = max([s for s, e, n in li])
for i in range(N):
    dfs(i, 0)
print(max(res))