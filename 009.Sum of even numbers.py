
def even_sum(n) :
    sum = 0
    for i in range(2,n+1,2) :
        sum += i
    return sum
print(even_sum(10))    

