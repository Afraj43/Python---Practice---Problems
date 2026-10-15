def reverse_string(s) :
    ans = ""
    for ch in s :
        ans = ch + ans
    return ans
print(reverse_string("hello"))    