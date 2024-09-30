def reverseString(s) -> None:
    """
    Do not return anything, modify s in-place instead.
    """
    f = 0
    length = len(s)
    l = length - 1 
    while f < l:
        temp = s[f]
        s[f] = s[l]
        s[l] = temp 
        f+=1
        l-=1

s = ["h","e","l","l","o","b"] 
reverseString(s)
print(s)