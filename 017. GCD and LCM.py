
def gcd_lcm(a,b) :
    x , y = abs(a) , abs(b) 

    while y != 0 :
     rem = x % y
     x = y 
     y = rem
    gcd = x
    
    if gcd == 0 :
        lcm = 0
    else :
        lcm = abs(a*b) // gcd 
        
    return gcd, lcm   
print(gcd_lcm(12,18)) 