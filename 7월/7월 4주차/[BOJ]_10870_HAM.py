# 피보나치수에 대한 이해

# 리스트로 접근해서, append로 하나씩 추가?
'''
p = list(int(input()))
# list로 감싸도 되는거지...?^^

for i in range(1, p+1) :
    total = 0
    for j in range(1, i+1) :
        total += j
'''  
      
# 삽질을 너무 많이 했고,,,^^,,,
# ... 재귀 함수. 함수만 보면 딱 알겠는데 공부를 더 해야될듯.
def fibo(n) :
    if n < 2 :
        return n
    else :
        return fibo(n-1) + fibo(n-2)

print(fibo(int(input())))
