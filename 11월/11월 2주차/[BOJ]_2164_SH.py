# 2164 카드 2
# 시간초과 때문에 덱 사용해야함(로직은 똑같)
from collections import deque

N = int(input())
# 리스트로 받아서 덱 만들어주기
deque = deque([i for i in range(1, N+1)])

while(len(deque) > 1):
    # 맨 처음에 하나 빼고 그 다음 숫자 젤 뒤로 붙여주기
    deque.popleft()
    tem = deque.popleft()
    deque.append(tem)

print(deque[0])

'''
내가 짠 시간초과 알고리즘
import sys
N = int(sys.stdin.readline())
arr = []

for i in range(N, 0, -1):
    arr.append(i)

while len(arr) >= 2:
    arr.pop()
    tem = arr.pop()
    arr.insert(0, tem)

print(arr[0])
'''