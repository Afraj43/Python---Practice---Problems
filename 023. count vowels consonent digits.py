def count_types(s) :
    vowels = 0
    consonents = 0
    digits = 0
    
    for ch in s.lower() :
        if ch.isdigit() :
            digits += 1
        elif ch.isalpha() :
            if ch in "aeiou" :
                vowels += 1
            else :
                consonents += 1
    return vowels , consonents , digits
print(count_types("afraj123"))                