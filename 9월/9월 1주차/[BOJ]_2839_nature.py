#2839 설탕 배달 

import sys

sugar = sys.stdin.readline

N = int(sugar())

sugar_bag = 0 # 설탕 봉지 수 

while N >= 0:
    if N % 5 == 0: # N이 5로 나누어 떨어질 때 
        sugar_bag += (N // 5) # 5로 나눈 값
        print(sugar_bag)
        break
    N -= 3 # N이 5의 배수 아닐 때 3을 빼줌
    sugar_bag += 1 # 3을 빼준 후 설탕 봉지 수를 1 증가시킴

else:
    print(-1)