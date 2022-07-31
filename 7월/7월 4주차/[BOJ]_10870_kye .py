#문제: n이 주어졌을 때, n번째 피보나치 수를 구하는 프로그램을 작성하시오.
#입력: 첫째 줄에 n이 주어진다. n은 20보다 작거나 같은 자연수 또는 0이다.
#출력; 첫째 줄에 n번째 피보나치 수를 출력한다.

#for loop 
n = int(input())
fibo_nums = [0, 1]

for i in range(2, n+1):   
    num = fibo_nums[i-1] + fibo_nums[i-2]  # Fn = Fn-1 + Fn-2 (n ≥ 2)
    fibo_nums.append(num)

print(fibo_nums[n])

#재귀함수(참고함)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))
