class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        index1 = 0
        index2 = 0

        while index1 < len(s):
            if index2 == len(t) :
                return False
            if s[index1] == t[index2]:
                index1 += 1 
            index2 += 1 
            print(index1, index2)
        return True 



s = "axc"
t = "ahbdgc"
solution = Solution()
print(solution.isSubsequence(s, t))