import sys
input = sys.stdin.readline

N = int(input())
ring = list(map(int, input().split()))

# 두 수의 최대공약수를 구하는 함수(유클리드 호제법)
def findGCD(a, b):
    num = b
    div = a
    rest = b % a
    while rest != 0:
        num = div
        div = rest
        rest = num % div
    return div

# i 번째 링 도는 횟수 = 첫 번째 링 반지름 / i 번째 링 반지름
# 2파이r / 2파이r' 형태에서, 2*파이는 약분되므로, 반지름만 고려해준다.
d = ring[0]
for idx in range(1, N):
    d_idx = ring[idx]
    GCD = findGCD(d, d_idx)
    print(f'{d//GCD}/{d_idx//GCD}')