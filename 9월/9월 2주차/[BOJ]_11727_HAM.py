# 10726과 차이점. 2*2까지 계산해줘야 됨.
import sys
input = sys.stdin.readline

n = int(input())

d = [0]*(n+1)
# 왜 공간을 이렇게 할당했을까.
# 리스트 만드는데 (n+1)개..?

d[1] = 1
if(n>=2):
    d[2] = 3
    for i in range(3, n+1) :
        d[i] = d[i-1]+(2*d[i-2])
        # 만들어진 점화식 사용..
print(d[n]%10007)