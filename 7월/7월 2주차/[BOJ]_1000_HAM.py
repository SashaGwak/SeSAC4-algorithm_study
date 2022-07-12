# A = int(input())
# B = int(input())

# print(A+B)
'''
첫째 줄에 A와 B가 주어진다고 했는데 두 줄에 걸쳐써서 오류.
'''

A, B = input().split()
print(int(A)+int(B))

# # split 활용. 쪼개서 입력받기
# 문자열.split(분류조건,나눌횟수)를 통해 리스트로 return함.
# split의 파라미터를 기본으로 하면 공백(띄어쓰기 탭 등)을 기반으로 분리하여 return 함.

# # map 활용 숫자 쪼개서 입력받기
# map함수는 map(적용할함수, 적용할 값)으로 활용.

# 한번에 A와 B 둘 다에 int함수를 씌울 수는 없나 순간 고민함.
