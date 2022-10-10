import sys

input = sys.stdin.readline

n = int(input())
stack = []

for _ in range(n):
    stack.append(int(input()))

last = stack[-1]
count = 1 # 맨 앞에 있는 막대기는 무조건 보이기 때문에 count의 초기값은 1이다.  

for i in reversed(range(n)):
    if stack[i] > last:
        count += 1
        last = stack[i] # 제일높은 막대기를 현재 막대기로 초기화
        
print(count)
