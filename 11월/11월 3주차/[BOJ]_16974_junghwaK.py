def getP( n, x ):
    if n==0:
        if x==0: return 0
        elif x==1: return 1  
    elif x==1:
        return 0
    elif x <= 1+h[n-1]:
        return getP( n-1, x-1 )
    elif x == 1+h[n-1]+1:
        return p[n-1]+1
    elif x <= 1+h[n-1]+1+h[n-1]:
        return p[n-1]+1+getP( n-1, x-(1+h[n-1]+1) )
    else:
        return p[n-1] + 1 + p[n-1]

n, x = map(int, input().split())
h = [1] * (n+1)
p = [1] * (n+1)

for i in range( 1, n+1 ):
    h[i] = 1 + h[i-1] + 1 + h[i-1] + 1
    p[i] = p[i-1] + 1 + p[i-1]
    
print( getP( n, x ) )