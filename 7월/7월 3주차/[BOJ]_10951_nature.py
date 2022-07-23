# 10951(A+B -4)

while True:
    try: 
        A, B = map(int, input().split())
        print(A + B)
    except:
        break

# try, except문
#   오류 처리를 위함 
#   try 블록 수행 중 오류가 발생하면 except 블록이 수행됨 