# 두 정수 A와 B를 입력받은 다음, A + B를 출력하는 프로그램을 작성하시오.
# 첫째 줄에 A와 B가 주어진다. ( 0 < A, B < 10 )
# 첫째 줄에 A + B를 출력한다.

# 1차 시도 - 오
A, B = input()
print(int(A) + int(B))

# 답

A, B = input().split()
print(int(A) + int(B))

# 알게된 점
# split() 함수를 이용해 입력받은 두 수를 떨어뜨려줘야 함
