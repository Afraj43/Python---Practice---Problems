
def leap_year(n) :
    return "Leap Year" if (n % 4 == 0 and n % 100 != 0) or (n % 400 == 0) else "Not Leap Year"

print(leap_year(1900))
