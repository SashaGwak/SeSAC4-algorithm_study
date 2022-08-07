# 17608 막대기

import sys
input = sys.stdin.readline

N = int(input())
sticks = []

for i in range(N): 
    sticks.append(int(input())) 
count = 0
last = 0
for j in reversed(sticks): # 역방향으로 각 문자에 접근하기 위해 사용
    if last < j: # 마지막 막대기보다 앞 막대기가 크다면
        last = j # 마지막 막대기는 앞 막대기가 되고 
        count += 1 # 숫자가 올라감

print(count)