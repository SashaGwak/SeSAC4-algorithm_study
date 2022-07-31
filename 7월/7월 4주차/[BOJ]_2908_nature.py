# 2908 상수
A, B = input().split()

A = int(A[::-1])
B = int(B[::-1])

if A > B :
    print(A)
else :
    print(B)

# [::-1]
# 문자열을 [::-1]로 호출하면 문자열을 뒤집은 결과를 반환