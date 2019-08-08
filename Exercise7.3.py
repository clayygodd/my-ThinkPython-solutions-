import math

def stair(x):
    if x == 0:
        result = 1
        return result
    else:
        result = x * stair(x-1)
        return result

def sig(x):
        
#    if x == 100:
#        result = 0
#        return result
#    else:       
        a = 4*stair(x)*(1103+26390*x)
        b = (stair(x)**4) * (396**(4*x))
        sigma = a/b
        while True:
            if sigma < 1e-15:
                break
            result += sigma
            x += 1
        return result

print sig(1)


pi = 9801/(2*math.sqrt(2)*sig(1))

print ('pi')




