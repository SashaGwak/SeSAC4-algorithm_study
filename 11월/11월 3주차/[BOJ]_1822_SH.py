# 1822 차집합 
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))

res = a - b

if res: 
    print(len(res))
    print(*sorted(list(res)))
else: 
    print(0)