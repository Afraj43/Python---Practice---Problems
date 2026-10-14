
def dec_to_bin(n) :
    if n == 0 :
        return '0'
    ans = ''
    while n :
        ans = str(n % 2) + ans
        n //= 2
    return ans
print(dec_to_bin(13))    