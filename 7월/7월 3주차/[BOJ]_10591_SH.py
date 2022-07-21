# A+B -4(10951번)
# 문제 
# 두 정수 A와 B를 입력받은 다음, A+B를 출력하는 프로그램을 작성하시오.
import sys

while True: 
    try:
        A, B = map(int, sys.stdin.readline().split())
        print(A + B)
    except:
        break
