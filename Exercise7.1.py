import math

def mysqrt(a,x): 
    while True:
        y = (x + a/x) / 2
        if y == x:
            break
        x = y
    return y
    

print('a mysqrt(a) math.sqrt(a) diff \n- --------- ------------ ----')



for i in range(1,10):
    a = mysqrt(float(i),1.0) 
    b = math.sqrt(float(i))
    c = a - b
    print i, a, b, c
    
