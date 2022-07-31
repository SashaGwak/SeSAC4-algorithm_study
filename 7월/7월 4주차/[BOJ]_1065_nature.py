N = int(input())
H = 0

for i in range(1, N+1):
    if i < 100 :
        H += 1
    else :
        n = list(map(int, str(i)))
        if n[0] - n[1] == n[1] - n[2]:
                 H += 1

print(H)

# 99까지 한수 
# 3자리 수부터는 백의 자리수와 십의 자리수의 차와 십의 자리수와 일의 자리수의 차가 같아야 한수