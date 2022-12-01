# 2992 크면서 작은 수

from itertools import permutations
import sys
input = sys.stdin.readline


X = list(input().rstrip())
x = int(''.join(X))
tmp = set()
for comb in permutations(X):
    if int(''.join(comb)) > x:
        tmp.add(int(''.join(comb)))
res = list(tmp)
res.sort()
if res:
    print(res[0])
else:
    print(0)
