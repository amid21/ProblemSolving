class Solution:
    def uniqueOccurrences(self, arr) -> bool:
        dict = {}
        for element in arr: 
            if element in dict: 
                dict[element] += 1
            else: 
                dict[element] = 1 
        print(dict)

        seen = set()
        for val in dict.values():
            if val in seen:
                return False
            else:
                seen.add(val)
        return True

    
solution = Solution()
arr = [1,2,2,1,1,3]
print(solution.uniqueOccurrences(arr))