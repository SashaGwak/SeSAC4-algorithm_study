#문제: 자연수 M과 N이 주어질 때 M이상 N이하의 자연수 중 소수인 것을 모두 골라 이들 소수의 합과 최솟값을 찾는 프로그램을 작성하시오.
#입력: 입력의 첫째 줄에 M이, 둘째 줄에 N이 주어진다. M과 N은 10,000이하의 자연수이며, M은 N보다 작거나 같다.
#출력: M이상 N이하의 자연수 중 소수인 것을 모두 찾아 첫째 줄에 그 합을, 둘째 줄에 그 중 최솟값을 출력한다. 
#단, M이상 N이하의 자연수 중 소수가 없을 경우는 첫째 줄에 -1을 출력한다.

"""
#한 개의 수 안에서 소수 찾기
n = 100

def isPrime(a):
    if(a<2):
        return False
    for i in range (2, a):
        if a%i == 0:
            return False
    return True

for i in range(n+1):
    if(isPrime(i)):
        print(i)

#두 수의 범위 안에서 소수 찾기
n = 1000
a = [False, False] + [True]*(n-1)
primes = []

for i in range(2, n+1):
    if a[i]:
        primes.append(i)
        for j in range(2*i, n+1, i):
            a[j] = False
print(primes)

"""
M = int(input())
N = int(input())
arr = []

for i in range(M, N+1):
    if i == 1:
        pass          #1은 소수가 아니다.
    elif i == 2:
        arr.append(i)
    else:
        for j in range(2, i):
            if i%j == 0:
                break            #1가 자가지신 외에 나눠떨어지면 소수가 아니다.
            elif j == i-1:       #j가 i-1까지 반복하여 i값이 반복 출력되는 것을 막는다.
                arr.append(i)
               
if len(arr)==0:    #M, N 사이에 소수가 없을 경우
    print('-1')
else:
    print(sum(arr))
    print(min(arr))
