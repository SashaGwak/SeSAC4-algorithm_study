# 팰린드롬 수(1259)
import sys

# 팰린드롬 확인하는 함수 생성 
def palindrome (str):
    flag = 1 
    for i in range(len(str)// 2): 
        if str[i] == str[len(str) - (i + 1)]:
            # 맨 끝수부터 순차적으로 모두 확인하도록! 
            # continue 안해주면 첫번째 값만 같아도 팰린드롬 맞는 것으로 판명나기 때문
            continue
        else: 
            flag = 0
            break
    
    if flag: 
        print('yes')
    else: 
        print('no')

while True: 
    comment = sys.stdin.readline().strip()
    if comment == '0': 
        break
    palindrome(comment)

# [::-1]해서 똑같은지 확인해주는 간단한 방법도 있답니다 ㅎ 