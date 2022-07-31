#10870 피보나치 수 5
A = int(input())

F = [ 0, 1 ]

for i in range(2, A+1):
    N = F[i-1] + F[i-2]
    F.append(N)
print(F[A])

# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) (n >= 2)