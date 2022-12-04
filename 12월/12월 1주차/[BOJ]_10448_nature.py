# 10448 유레카이론

T = [n * (n+1) // 2 for n in range(1, 46)]
E = [0]*1001

for i in T:
    for j in T:
        for k in T:
            if i+j+k <= 1000:
                E[i+j+k] = 1

for i in range(int(input())):
    print(E[int(input())])