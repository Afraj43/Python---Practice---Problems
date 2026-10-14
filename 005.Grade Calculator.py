
def grade_calculator(n) :
    if n >= 80 :
        return "A+"
    elif n >= 75 and n < 80 :
        return "A-"
    elif n >= 70 and n < 75 :
        return "A"
    elif n >= 65 and n < 70 :
        return "B+"
    elif n >= 60 and n < 65 :
        return "B-"
    elif n >= 55 and n < 60 :
        return "B"
    elif n >= 50 and n < 55 :
        return "C+"
    elif n >= 45 and n < 50 :
        return "C-"
    elif n >= 40 and n < 45 :
        return "C"
    else :
        return "Fail"
print(grade_calculator(56))    