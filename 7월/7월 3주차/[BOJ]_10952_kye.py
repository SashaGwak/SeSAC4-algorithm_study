"""
list_A = [1, 2, 3, 9, 5, 0]
list_B = [1, 3, 4, 8, 2, 0]

print(list_A[0]+list_B[0])
print(list_A[1]+list_B[1])
print(list_A[2]+list_B[2])
print(list_A[3]+list_B[3])
print(list_A[4]+list_B[4])
print(list_A[5]+list_B[5])
"""

list_A = []
list_B = []

for i in range ( 5 ):
    input_A = int(input("0보다 큰 정수 A를 입력하세요."))
    list_A.append(input_A)
    input_B = int(input("10보다 작은 정수 B를 입력하세요."))
    list_B.append(input_B)
    print(list_A[i] + list_B[i])

print("list_A: ", list_A)
print("list_B: ", list_B)




"""

fruit_list = []
for i in range (1,4):
    fruit = input('3개의 과일 입력(현재{i}번 째):')
    fruit_list.append(fruit)
print(fruit_list)
"""
