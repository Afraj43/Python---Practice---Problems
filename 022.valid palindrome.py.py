def valid_palindrome(s) :
    ans = ""
    for ch in s :
        if ch.isalnum() :
            ans += ch.lower()
    return ans == ans[::-1]    
print(valid_palindrome("a man a man"))    