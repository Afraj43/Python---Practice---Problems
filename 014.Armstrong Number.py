
def armstrong(n) :
    n = abs(n)
    original = n
    sum = 0 
    
    while n > 0 :
        digit = n % 10
        sum +=  digit**3
        n = n // 10
    if original == sum :
        print("Armstrong")   
    else :
        print("Not Armstrong")   
armstrong(765)     