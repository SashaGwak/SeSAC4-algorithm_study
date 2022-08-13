# 1259 팰린드롬 수

while(True): 
    a = input() # ex) radar
    if a == a[::-1]: # ex) radar == radar
        print("yes")
    elif a == "0": # 0이면 출력 x
        break
    else: 
        print("no")