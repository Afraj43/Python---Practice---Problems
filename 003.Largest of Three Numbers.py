
def largest(a,b,c) :
    ans = a 
    
    if b > ans :
        ans = b 
    if c > ans :
        ans = c
    return ans 
print(largest(10,20,8))      