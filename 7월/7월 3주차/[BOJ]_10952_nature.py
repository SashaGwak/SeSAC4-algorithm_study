#10952(A+B -5) 

while True:
    A, B = map(int, input().split())
    if ( A == 0 and B == 0 ):
        break
    else:
        print(A + B)

# while문 
#     while <조건문>:
#         <수행할 문장1>
#         <수행할 문장2>
#         ...
#     조건문이 참이면 무한반복

# break문
#   while문을 강제로 빠져나갈 수 있음