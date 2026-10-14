
def sum_of_digit(n) :
    sum = 0
    n = abs(n) 
    while n > 0 :
        last_digit = n % 10
        sum += last_digit
        n = n // 10
    return sum 
print(sum_of_digit(-12345))    
