class Solution:
    def reverseWords(self, s: str) -> str:
        # arr = s.split()
        # arr = arr[::-1]
        # arr = ' '.join(arr)
        # print(arr)
        arr = []
        temp = ''
        for c in s:
            if c != " ":
                temp += c
            elif temp != '':
                arr.append(temp)
                temp = ''
        if temp != '':
            arr.append(temp)
        print(arr)
        arr = ' '.join(arr[::-1])
        print(arr)





s = "the sky  is blue  "
solution = Solution()
solution.reverseWords(s)
