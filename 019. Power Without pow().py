
def power(a,b) :
    ans = 1
    
    for i in range(b) :
        ans = ans * a
    return ans
print(power(2,3))