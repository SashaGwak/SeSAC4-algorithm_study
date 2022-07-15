# 10869 사칙연산

# 1차 시도
A, B = input().split()
print(int(A)+int(B))
print(int(A)-int(B))
print(int(A)*int(B))
print(int(A)/int(B))
print(int(A)%int(B))

# 2차 시도
A, B = input().split()
print(int(A)+int(B))
print(int(A)-int(B))
print(int(A)*int(B))
print(int(A)//int(B))
print(int(A)%int(B))

# 답
A, B = map(int, input().split())
print(A+B)
print(A-B)
print(A*B)
print(A//B)
print(A%B)

# 알게된 점
# map() 
# map(함수, 반복 가능한 객체)
# 반복 가능한 객체의 요소들에 함수를 적용하는 역할을 해줌
# // - 나누기에도 두번 쓰게 될 줄 몰랐음