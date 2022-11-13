# 3036 링

from math import gcd # gcd - 인자로 들어온 숫자들의 최대 공약수를 반환

N = int(input()) # 링의 개수 
R = list(map(int, input().split())) # 링의 반지름

for i in range(1, N): # 총 N-1줄 출력
    C = gcd(R[0], R[i]) # 첫번째 링과 다른 링의 최대 공약수
    print(f'{R[0] // C}/{R[i] // C}') 
    # 분자 - {R[0] // C}
        # 첫 번째 링의 반지름이 8,두 번째 링의 반지름이 4라면
        # 8 // 4 = 2
    # 분모 - {R[i] // C}
        # 4 // 4 = 1
    # => 2/1