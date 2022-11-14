import sys
input = sys.stdin.readline

N = int(input()) # 링의 개수

li = list(map(int, input().split())) # 링 수

# 최대 공약수. 유클리드 호제법 사용.
def GCD(a,b) : # 항상 a 가 큰수
    while b!=0 :
        remain = a % b
        a = b
        b = remain

    return a

target = li.pop(0)

for i in range(N-1) :
    num = GCD(target, li[i])
    # print formatting 
    print('{}/{}'.format(target//num, li[i]//num))