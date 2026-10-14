def simple_calculator(a , b , op ) :
    if op == "+" :
        return a + b
    elif op == "-" :
        return a - b
    elif op == "*" :
        return a * b
    elif op == "/" :
        return a / b if b != 0 else  "division by zero"
    else : 
        return "Invalid operation"
print(simple_calculator(5 , 8 , "/"))    
