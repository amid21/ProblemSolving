def reverseWords(s: str) -> str:
    arr = s.split(" ")
    #return ' '.join(arr[::-1])
    return s.split()
s = "   the sky     is blue   "
result = reverseWords(s)
print(result)