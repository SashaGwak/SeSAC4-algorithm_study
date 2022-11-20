# 1822 차집합

nA, nB = map(int, input().split()) # 집합 A의 원소의 개수와 집합 B의 원소의 개수

A = set(map(int, input().split()))
B = set(map(int, input().split()))

print(len(A-B)) # 차집합의 원소의 개수 출력
print(*sorted(list(A-B))) # 차집합의 원소(증가하는 순서로 출력)
