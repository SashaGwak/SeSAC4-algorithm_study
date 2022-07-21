#두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
#입력의 마지막에는 0 두 개가 온다.

list_A = []
list_B = []

for i in range ( 5 ):
    input_A = int(input("0보다 큰 정수 A를 입력하세요."))
    list_A.append(input_A)
    input_B = int(input("10보다 작은 정수 B를 입력하세요."))
    list_B.append(input_B)
    print(list_A[i] + list_B[i])

print(0, 0)
