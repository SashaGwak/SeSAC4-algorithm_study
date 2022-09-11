#11726 2 x n 타일링

N = int(input())

L = [0] * 1001 # memoization

L[1] = 1
L[2] = 2

for i in range(3, 1001):
    L[i] = L[i-1] + L[i-2]

print(L[N] % 10007) 

#memoization 

# 동적 계획법 알고리즘에서 핵심이 되는 기술
# 중복 계산을 제거함으로써 프로그램의 전체적인 실행 속도를 빠르게, 성능을 향상할 수 있는 기법

# ex) 피보나치 수 => 재귀 트리에서 노드 두 번 이상 나타남
# 이때 memoization을 사용하면 반복 작업을 피할 수 있음