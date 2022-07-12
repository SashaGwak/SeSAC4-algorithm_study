# 사칙연산
# 입력 
# 두 자연수 A와 B가 주어진다. (1 ≤ A, B ≤ 10,000)
# 출력
# 첫째 줄에 A+B, 둘째 줄에 A-B, 셋째 줄에 A*B, 넷째 줄에 A/B, 다섯째 줄에 A%B를 출력한다.
A, B = map(int, input().split())

print(A + B, A - B, A * B, A // B, A % B, sep='\n')

# print()의 옵션 
# 1. sep(separation) : 분리하여 출력, 다만 갈라놓을 문자를 지정할 수 있다(구분자)
# 2. end : 그 뒤의 출력값과 이어서 출력한다
#   ex. print("I Like, end=" ")
#       print("SeSAC")          >> I Like SeSAC 

