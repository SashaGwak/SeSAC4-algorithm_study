#10809(알파벳 찾기)

#1 - 아스키코드 이용
string = input()
alphabet = list(range(97,123))

for i in alphabet:
    print(string.find(chr(i)))

# 아스키코드 97 ~ 122 = a ~ z

# list(range(97, 123))
# [97, 98, ..., 122]

# find()
# 입력한 문자가 첫번째 위치한 자리를 출력
# 찾는 문자가 없는 경우 -1을 출력 

# chr()
# 하나의 정수(아스키코드)를 인자로 받고 해당 정수에 해당하는 유니코드 문자를 반환
# ex) chr(97) -> 'a' 반환

#2

string = input()
alphabet = "abcdefghijklmnopqrstuvwxyz"
for i in alphabet:
    print(string.find(i), end = ' ')

# end = ' '
# 쓰지 ❌ : 세로로 출력
# 쓰면 ⭕️ : 가로로 출력