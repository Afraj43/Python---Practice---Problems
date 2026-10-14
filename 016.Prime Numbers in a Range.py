
def prime_in_range(L,R) :
    result = []
    def prime_number(n) :
            if n < 2 :
                return False 
            i = 2
            while i * i <= n :
                if n % i == 0 :
                    return False 
                i += 1
            return True    
    for i in range(L, R+1) :
        if prime_number(i) :
            result.append(i)
    return result      
print(prime_in_range(10,30))  