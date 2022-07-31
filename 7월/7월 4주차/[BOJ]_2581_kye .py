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
        pass
    elif i == 2:
        arr.append(i)
    else:
        for j in range(2, i):
            if i%j == 0:
                break
            elif j == i-1:
                arr.append(i)
               
if len(arr)==0:
    print('-1')
else:
    print(sum(arr))
    print(min(arr))
