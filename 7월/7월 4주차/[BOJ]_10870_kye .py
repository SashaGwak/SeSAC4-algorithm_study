#for loop 
n = int(input())
fibo_nums = [0, 1]

for i in range(2, n+1):
    num = fibo_nums[i-1] + fibo_nums[i-2]
    fibo_nums.append(num)

print(fibo_nums[n])

#재귀함수(참고함)
def fibonacci(n):
    if n <= 1:
        return n
    return fibonacci(n-1) + fibonacci(n-2)

n = int(input())
print(fibonacci(n))

