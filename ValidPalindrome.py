import re 
def isPalindrome(s: str):
    s = s.lower()
    s = re.sub(r'\a-zA-z0-9','',s)
    print(s)
    print(s[::-1])
    return s == s[::-1]

s = "ab_a"
s = isPalindrome(s)



