def f(n):
    if n == 0 or n == 1:
        return n

    else:
        return f(n-1) + f(n-2)

n = int(input())
print(f(n))
